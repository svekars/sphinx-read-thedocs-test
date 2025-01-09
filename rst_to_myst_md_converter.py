import argparse
import asyncio
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import aiohttp
import anthropic
import tiktoken


def count_tokens(text: str) -> int:
    """
    Count tokens in text using cl100k_base encoding (used by Claude)
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def split_rst_content(content: str, max_tokens: int = 3500) -> List[str]:
    """
    Split RST content into chunks that respect structure while staying under token limit.
    """
    chunks = []
    current_chunk = []
    current_tokens = 0

    lines = content.splitlines(True)

    def flush_chunk():
        nonlocal current_chunk, current_tokens
        if current_chunk:
            chunks.append("".join(current_chunk))
            current_chunk = []
            current_tokens = 0

    for i, line in enumerate(lines):
        line_tokens = count_tokens(line)

        if current_tokens + line_tokens > max_tokens:
            if i > 0 and re.match(r"^[-=^~]+$", lines[i - 1].strip()):
                flush_chunk()
            elif not line.strip():
                flush_chunk()
            elif current_tokens > max_tokens:
                flush_chunk()

        current_chunk.append(line)
        current_tokens += line_tokens

    flush_chunk()
    return chunks


class RSTToMarkdownConverter:
    def __init__(self):
        self.is_first_chunk = False
        self.is_last_chunk = False

    def set_chunk_position(self, is_first: bool, is_last: bool):
        self.is_first_chunk = is_first
        self.is_last_chunk = is_last

    def convert_links(self, content: str) -> str:
        """Convert RST links to Markdown format."""
        # Convert external links with text: `text <url>`_ -> [text](url)
        content = re.sub(
            r"`([^`]+)\s+<([^>]+)>`_",
            lambda m: f"[{m.group(1)}]({m.group(2)})",
            content,
        )

        # Convert simple links: `text`_ -> [text](text)
        content = re.sub(
            r"`([^`]+)`_", lambda m: f"[{m.group(1)}]({m.group(1)})", content
        )

        return content

    def convert_heading(self, content: str) -> str:
        """Convert RST headings to Markdown headings based on order of appearance."""
        lines = content.splitlines()
        converted_lines = []

        # Dictionary to store the mapping of underline style to heading level
        style_to_level = {}

        # First pass: determine hierarchy
        i = 0
        while i < len(lines) - 1:
            line = lines[i]
            next_line = lines[i + 1]

            # Check if this is a heading (text followed by underline)
            if (
                line.strip()  # Non-empty line
                and re.match(r"^[-=^~_]+$", next_line.strip())  # Underline line
                and len(next_line.strip()) >= len(line.strip())
            ):  # Underline at least as long as text

                underline_char = next_line.strip()[0]

                # If this is the first heading we've seen
                if not style_to_level:
                    if underline_char == "=" or self.is_first_chunk:
                        style_to_level[underline_char] = 1
                    else:
                        style_to_level[underline_char] = 2
                # For subsequent headings
                elif underline_char not in style_to_level:
                    style_to_level[underline_char] = len(style_to_level) + (
                        1 if self.is_first_chunk else 2
                    )

            i += 1

        # Second pass: convert headings
        i = 0
        while i < len(lines):
            line = lines[i]

            # Check for underline-style headers
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if re.match(r"^[-=^~_]+$", next_line.strip()) and len(
                    next_line.strip()
                ) >= len(line.strip()):

                    underline_char = next_line.strip()[0]
                    if underline_char in style_to_level:
                        level = style_to_level[underline_char]
                        converted_lines.append("#" * level + " " + line)
                        i += 2
                        continue

            converted_lines.append(line)
            i += 1

        # Debug output
        print(f"Style to level mapping: {style_to_level}")

        return "\n".join(converted_lines)

    def remove_rst_labels(self, content: str) -> str:
        """Remove RST cross-reference labels."""
        return re.sub(r"\.\. _[\w-]+:\n\n", "", content)

    def convert_contents_directive(self, content: str) -> str:
        """Convert contents directive to MyST format."""
        pattern = r"\.\.?\s+contents::(?:\s+(.*?))?\n(?:\s+:(.*?):\s*(.*?)\n)*"

        def replacement(match):
            title = match.group(1) or ""
            options_text = match.string[match.start() : match.end()]

            # Extract options
            options = {}
            for line in options_text.split("\n"):
                option_match = re.match(r"\s+:([^:]+):\s*(.*)", line)
                if option_match:
                    key, value = option_match.groups()
                    options[key.strip()] = value.strip()

            # Build MyST format
            myst_content = "```{contents}"
            if title:
                myst_content += f" {title.strip()}"
            myst_content += "\n"

            # Add options
            for key, value in options.items():
                myst_content += f":{key}: {value}\n"

            myst_content += "```"
            return myst_content

        return re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)

    def convert_autodoc_directive(self, content: str) -> str:
        """Convert autodoc and autosummary directives to MyST format."""

        lines = content.splitlines()
        result_lines = []
        in_autosummary = False
        current_block = []

        i = 0
        while i < len(lines):
            line = lines[i]

            # Start of autosummary block
            if line.strip().startswith(".. autosummary::"):
                if in_autosummary:
                    # Flush previous block if we were in one
                    if current_block:
                        result_lines.append("```{eval-rst}")
                        result_lines.extend(current_block)
                        result_lines.append("```")
                        result_lines.append("")
                        current_block = []

                in_autosummary = True
                current_block = [line]
                i += 1

                # Collect options (lines starting with :)
                while i < len(lines) and lines[i].strip().startswith(":"):
                    current_block.append(lines[i])
                    i += 1

                # Skip blank lines
                while i < len(lines) and not lines[i].strip():
                    current_block.append(lines[i])
                    i += 1

                # Collect indented content
                while i < len(lines) and (
                    not lines[i].strip() or lines[i].startswith("    ")
                ):
                    current_block.append(lines[i])
                    i += 1

                # Flush the block
                result_lines.append("```{eval-rst}")
                result_lines.extend(current_block)
                result_lines.append("```")
                result_lines.append("")

                in_autosummary = False
                current_block = []
                continue

            result_lines.append(line)
            i += 1

        # Flush any remaining block
        if current_block:
            result_lines.append("```{eval-rst}")
            result_lines.extend(current_block)
            result_lines.append("```")
            result_lines.append("")

        return "\n".join(result_lines)

    def convert_automodule_directive(self, content: str) -> str:
        """Convert automodule directives to MyST format."""

        def process_automodule(match):
            full_block = match.group(0).rstrip()
            return f"```{{eval-rst}}\n{full_block}\n```\n"

        automodule_pattern = r"\.\.?\s+automodule::\s*[^\n]+(?:\n\s+:[^\n]+)*"
        content = re.sub(
            automodule_pattern, process_automodule, content, flags=re.MULTILINE
        )
        return content

    def convert_currentmodule_directive(self, content: str) -> str:
        """Convert currentmodule directives to MyST format."""

        def process_currentmodule(match):
            full_block = match.group(0).rstrip()
            return f"```{{eval-rst}}\n{full_block}\n```\n"

        currentmodule_pattern = r"\.\.?\s+currentmodule::\s*[^\n]+"
        content = re.sub(
            currentmodule_pattern, process_currentmodule, content, flags=re.MULTILINE
        )
        return content

    def convert_other_directives(self, content: str) -> str:
        """Convert other common directives to MyST format."""
        # Convert figure directive
        content = re.sub(
            r"\.\.?\s+figure::\s*(.*?)(?=\n\n|$)",
            lambda m: f"```{{figure}} {m.group(1)}```",
            content,
            flags=re.DOTALL,
        )

        # Convert image directive
        content = re.sub(
            r"\.\.?\s+image::\s*(.*?)(?=\n\n|$)",
            lambda m: f"```{{image}} {m.group(1)}```",
            content,
            flags=re.DOTALL,
        )

        # Convert math directive
        content = re.sub(
            r"\.\.?\s+math::\s*(.*?)(?=\n\n|$)",
            lambda m: f"```{{math}}\n{m.group(1)}\n```",
            content,
            flags=re.DOTALL,
        )

        return content

    def convert_cross_references(self, content: str) -> str:
        """Convert cross-references to MyST format."""
        ref_patterns = {
            r":py:class:`([^`]+)`": r"{py:class}`\1`",
            r":py:func:`([^`]+)`": r"{py:func}`\1`",
            r":py:meth:`([^`]+)`": r"{py:meth}`\1`",
            r":py:mod:`([^`]+)`": r"{py:mod}`\1`",
            r":py:attr:`([^`]+)`": r"{py:attr}`\1`",
            r":py:data:`([^`]+)`": r"{py:data}`\1`",
            r":py:exc:`([^`]+)`": r"{py:exc}`\1`",
            r":py:obj:`([^`]+)`": r"{py:obj}`\1`",
            r":doc:`([^`]+)`": r"{doc}`\1`",
            r":ref:`([^`]+)`": r"{ref}`\1`",
            r":title:`([^`]+)`": r"{title}`\1`",
            r":numref:`([^`]+)`": r"{numref}`\1`",
            r":cpp:class:`([^`]+)`": r"{cpp:class}`\1`",
            r":cpp:func:`([^`]+)`": r"{cpp:func}`\1`",
        }

        for pattern, replacement in ref_patterns.items():
            content = re.sub(pattern, replacement, content)
        return content

    def convert_role_directive(self, content: str) -> str:
        """Convert role directives to MyST format."""

        def process_role(match):
            full_block = match.group(0).rstrip()
            return f"```{{eval-rst}}\n{full_block}\n```\n"

        role_pattern = (
            r"\.\.?\s+role::\s*[^\n]+"  # directive start
            r"(?:\s*\n\s+:[^\n]+)*"  # options
        )
        content = re.sub(role_pattern, process_role, content, flags=re.MULTILINE)
        return content

    def convert_admonitions(self, content: str) -> str:
        """Convert admonition directives to MyST format."""
        admonition_types = [
            "warning",
            "note",
            "attention",
            "caution",
            "danger",
            "error",
            "hint",
            "important",
            "seealso",
            "tip",
            "todo",
        ]

        for admonition in admonition_types:
            pattern = f".. {admonition}::(.*?)(?=\n\n|$)"
            content = re.sub(
                pattern,
                lambda m: f"```{{{admonition}}}\n{m.group(1).strip()}\n```",
                content,
                flags=re.DOTALL,
            )

        # Convert generic admonition
        content = re.sub(
            r"\.\.?\s+admonition::\s*(.*?)(?=\n\n|$)",
            lambda m: f"```{{admonition}} {m.group(1)}```",
            content,
            flags=re.DOTALL,
        )

        return content

    def convert_comments(self, content: str) -> str:
        """Convert RST comments to HTML comments, but ignore autodoc directives."""

        def is_special_directive(line):
            special_patterns = [
                r"\.\.?\s+automodule::",
                r"\.\.?\s+autoclass::",
                r"\.\.?\s+autofunction::",
                r"\.\.?\s+automethod::",
                r"\.\.?\s+autoattribute::",
                r"\.\.?\s+autodata::",
                r"\.\.?\s+autoexception::",
                r"\.\.?\s+autoproperty::",
                r"\.\.?\s+autosummary::",
                r"\.\.?\s+currentmodule::",
                r"\.\.?\s+role::",
                r"\s+:toctree:",
                r"\s+:nosignatures:",
                r"\s+:template:",
                r"\s+:class:",
                r"\s+~[\w\.]+",
            ]
            return any(re.match(pattern, line) for pattern in special_patterns)

        lines = content.splitlines()
        converted_lines = []

        i = 0
        while i < len(lines):
            line = lines[i]
            if is_special_directive(line):
                converted_lines.append(line)
                i += 1
                continue

            if line.strip().startswith(".."):
                # Check if it's a single-line comment
                if not any(
                    line.strip().startswith(".. " + x)
                    for x in [
                        "figure::",
                        "image::",
                        "math::",
                        "include::",
                        "toctree::",
                        "contents::",
                        "role::",
                    ]
                ):
                    converted_lines.append(f"<!-- {line.strip()[3:]} -->")
                else:
                    converted_lines.append(line)
            else:
                converted_lines.append(line)
            i += 1

        return "\n".join(converted_lines)

    def convert_toctree(self, content: str) -> str:
        """Convert toctree directives if present in original RST."""
        pattern = r"(\.\.?\s+toctree::.*?(?=\n\n|$))"
        return re.sub(
            pattern, lambda m: f"```{m.group(1)}```", content, flags=re.DOTALL
        )

    def convert(self, content: str) -> str:
        """Apply all conversion rules in sequence."""
        content = self.convert_heading(content)
        content = self.remove_rst_labels(content)
        content = self.convert_role_directive(content)
        content = self.convert_automodule_directive(content)
        content = self.convert_currentmodule_directive(content)
        content = self.convert_contents_directive(content)
        content = self.convert_autodoc_directive(content)
        content = self.convert_other_directives(content)
        content = self.convert_admonitions(content)
        content = self.convert_cross_references(content)
        content = self.convert_links(content)
        content = self.convert_comments(content)
        content = self.convert_toctree(content)
        return content


class CodeResolver:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self._cache: Dict[str, Optional[Tuple[str, Path]]] = {}

    def _extract_definition(
        self, content: str, name: str, start_idx: int, file_path: Path
    ) -> Optional[Tuple[str, Path]]:
        """Extract relevant code definition and docstring"""
        lines = content[start_idx : start_idx + 2000].split("\n")
        definition_lines = []
        indent = None

        for line in lines:
            if not definition_lines:
                definition_lines.append(line)
                # Detect indentation of first line after definition
                if line.startswith("def ") or line.startswith("class "):
                    indent = len(line) - len(line.lstrip())
                continue

            current_indent = len(line) - len(line.lstrip())
            if line.strip() == "" or current_indent > indent:
                definition_lines.append(line)
            else:
                break

        if definition_lines:
            return "\n".join(definition_lines), file_path
        return None

    def find_in_code(self, identifier: str) -> Optional[Tuple[str, Path]]:
        """
        Try to find a Python object (function, class, etc) in the codebase
        Returns (content, file_path) if found, None otherwise
        """
        if identifier in self._cache:
            return self._cache[identifier]

        parts = identifier.split(".")

        # Common PyTorch module locations to search
        search_paths = [
            self.repo_root / "torch",
            self.repo_root / "torch/nn",
            self.repo_root / "torch/nn/functional",
            self.repo_root / "torch/jit",
            self.repo_root / "torch/distributions",
            self.repo_root / "torch/cuda",
            self.repo_root / "torch/utils",
        ]

        for base_path in search_paths:
            # Try as a module file
            potential_paths = [
                base_path / "/".join(parts[:-1]) / f"{parts[-1]}.py",
                base_path / "/".join(parts[:-1]) / "__init__.py",
                base_path / "/".join(parts) / "__init__.py",
            ]

            for path in potential_paths:
                if path.exists():
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            content = f.read()
                            # Look for class or function definition
                            obj_name = parts[-1]
                            patterns = [
                                f"class {obj_name}[:\(]",
                                f"def {obj_name}[:\(]",
                            ]
                            for pattern in patterns:
                                match = re.search(pattern, content)
                                if match:
                                    result = self._extract_definition(
                                        content, obj_name, match.start(), path
                                    )
                                    if result:
                                        self._cache[identifier] = result
                                        return result
                    except Exception as e:
                        print(f"Error reading {path}: {e}")
                        continue

        self._cache[identifier] = None
        return None


async def convert_rst_chunk_to_markdown(
    client: anthropic.AsyncAnthropic,
    rst_content: str,
    resolver: CodeResolver,
    is_first_chunk: bool = False,
    is_last_chunk: bool = False,
) -> str:
    """Convert RST content to Markdown using PyThon-based converter"""

    # Initialize converter
    converter = RSTToMarkdownConverter()
    converter.set_chunk_position(is_first_chunk, is_last_chunk)

    # Convert content
    try:
        converted_content = converter.convert(rst_content)
        return converted_content
    except Exception as e:
        print(f"Error in conversion: {str(e)}")
        # Fallback to Claude if conversion fails
        return await fallback_to_claude(client, rst_content)


async def fallback_to_claude(client, rst_content):
    """Fallback to using Claude for conversion if the Python converter fails"""
    message = await client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": f"Convert this RST to Markdown:\n\n{rst_content}",
            }
        ],
    )
    return message.content[0].text


async def process_file(
    client: anthropic.AsyncAnthropic,
    rst_file: Path,
    output_dir: Path,
    resolver: CodeResolver,
    show_content: bool = False,
) -> None:
    """
    Process a single RST file and save its Markdown conversion
    """
    try:
        print(f"\nProcessing: {rst_file}")

        # Read RST content
        with open(rst_file, "r", encoding="utf-8") as f:
            rst_content = f.read()

        if show_content:
            print("\nOriginal RST content (first 500 chars):")
            print("-" * 80)
            print(rst_content[:500] + "..." if len(rst_content) > 500 else rst_content)
            print("-" * 80)

        # Split content into chunks
        chunks = split_rst_content(rst_content)
        print(f"Split into {len(chunks)} chunks")

        # Convert each chunk
        markdown_chunks = []
        for i, chunk in enumerate(chunks):
            print(
                f"  Converting chunk {i+1}/{len(chunks)} ({count_tokens(chunk)} tokens)"
            )
            try:
                markdown_chunk = await convert_rst_chunk_to_markdown(
                    client,
                    chunk,
                    resolver,
                    is_first_chunk=(i == 0),
                    is_last_chunk=(i == len(chunks) - 1),
                )
                markdown_chunks.append(markdown_chunk)
            except Exception as e:
                print(f"  ✗ Error converting chunk {i+1}: {str(e)}")
                continue

        if not markdown_chunks:
            raise Exception("No chunks were successfully converted")

        # Combine chunks
        full_markdown = "\n\n".join(markdown_chunks)

        # Create output filename
        relative_path = rst_file.with_suffix(".md").name
        output_path = output_dir / relative_path

        # Save Markdown content
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_markdown)

        if show_content:
            print("\nConverted Markdown content (first 500 chars):")
            print("-" * 80)
            print(
                full_markdown[:500] + "..."
                if len(full_markdown) > 500
                else full_markdown
            )
            print("-" * 80)

        print(f"✓ Saved to {output_path}")

    except Exception as e:
        print(f"✗ Error processing {rst_file}: {str(e)}")
        raise


async def main():
    parser = argparse.ArgumentParser(
        description="Convert RST files to Markdown using Claude API"
    )
    parser.add_argument(
        "-n",
        "--num-files",
        type=int,
        help="Number of files to process (default: all files)",
    )
    parser.add_argument(
        "--show-content",
        action="store_true",
        help="Show sample of original and converted content",
    )
    parser.add_argument(
        "--debug", action="store_true", help="Show detailed error information"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Path to PyTorch repository root",
    )
    args = parser.parse_args()

    # Check for API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Create output directory
    output_dir = Path("llm")
    output_dir.mkdir(exist_ok=True)

    # Initialize Claude client and code resolver
    client = anthropic.AsyncAnthropic(api_key=api_key)
    resolver = CodeResolver(args.repo_root)

    excluded_dirs = {
        "_templates",
        "_static",
        "generated",
        "build",
        "_build",
        "venv",
        "env",
        ".git",
    }

    # Get list of RST files using ripgrep output
    rst_files = []

    for line in sys.stdin:
        path = Path(line.strip())
        # Check if any parent directory is in excluded_dirs
        if not any(part in excluded_dirs for part in path.parts):
            rst_files.append(path)

    if not rst_files:
        print("No RST files found in input", file=sys.stderr)
        sys.exit(1)

    total_files = len(rst_files)
    print(f"Found {total_files} total RST files")

    # Limit number of files if specified
    if args.num_files:
        rst_files = rst_files[: args.num_files]
        print(f"Processing {len(rst_files)} of {total_files} files:")
    else:
        print(f"Processing all {total_files} files:")

    for f in rst_files:
        print(f"- {f}")

    # Process files sequentially to better handle errors
    successful = 0
    failed = 0

    for i, rst_file in enumerate(rst_files, 1):
        try:
            print(f"\nProcessing file {i}/{len(rst_files)}")
            await process_file(
                client, rst_file, output_dir, resolver, args.show_content
            )
            successful += 1
        except Exception as e:
            failed += 1
            if args.debug:
                import traceback

                print(traceback.format_exc())
            else:
                print(f"✗ Error processing {rst_file}: {str(e)}")

    print(f"\nConversion complete!")
    print(f"Successfully converted: {successful} files")
    print(f"Failed conversions: {failed} files")
    print(f"Output directory: {output_dir.absolute()}")


if __name__ == "__main__":
    asyncio.run(main())
