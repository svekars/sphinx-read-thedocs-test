# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import re
import os
import torch



project = 'PyTorch Sphinx Theme 2'
copyright = '2024, PyTorch Contributors'
author = 'PyTorch Contributors'
release = '0.0.1'
master_doc = "index"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = [".rst", ".md"]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    "sphinx_design",
]

katex_css_path = \
    'https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css'
katex_js_path = 'katex.min.js'
katex_autorender_path = 'auto-render.min.js'
katex_inline = [r'\(', r'\)']
katex_display = [r'\[', r'\]']
katex_prerender = True
katex_options = ''

# build the templated autosummary files
autosummary_generate = True
numpydoc_show_class_members = False

# Disable docstring inheritance
autodoc_inherit_docstrings = False

# Show type hints in the description
autodoc_typehints = "description"

# Add parameter types if the parameter is documented in the docstring
autodoc_typehints_description_target = "documented_params"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

html_context = {
    "feedback_url": "https://github.com/pytorch/pytorch/", # update to your project
}

# Type aliases for common types
# Sphinx type aliases only works with Postponed Evaluation of Annotations
# (PEP 563) enabled (via `from __future__ import annotations`), which keeps the
# type annotations in string form instead of resolving them to actual types.
# However, PEP 563 does not work well with JIT, which uses the type information
# to generate the code. Therefore, the following dict does not have any effect
# until PEP 563 is supported by JIT and enabled in files.
autodoc_type_aliases = {
    "_size_1_t": "int or tuple[int]",
    "_size_2_t": "int or tuple[int, int]",
    "_size_3_t": "int or tuple[int, int, int]",
    "_size_4_t": "int or tuple[int, int, int, int]",
    "_size_5_t": "int or tuple[int, int, int, int, int]",
    "_size_6_t": "int or tuple[int, int, int, int, int, int]",
    "_size_any_opt_t": "int or None or tuple",
    "_size_2_opt_t": "int or None or 2-tuple",
    "_size_3_opt_t": "int or None or 3-tuple",
    "_ratio_2_t": "float or tuple[float, float]",
    "_ratio_3_t": "float or tuple[float, float, float]",
    "_ratio_any_t": "float or tuple",
    "_tensor_list_t": "Tensor or tuple[Tensor]",
}

from sphinx.ext.autosummary import Autosummary
from docutils import nodes
class CustomAutosummary(Autosummary):
    def get_table(self, items):
        table = super().get_table(items)
        # Assuming `table` is a `docutils.nodes.table` instance
        # Add a header row here
        header_row = nodes.row()
        header_row += [nodes.entry('', nodes.paragraph(text='Name'))]
        header_row += [nodes.entry('', nodes.paragraph(text='Description'))]
        if isinstance(table[0], nodes.tbody):
            table[0].insert(0, header_row)
        return table

# Enable overriding of function signatures in the first line of the docstring.
autodoc_docstring_signature = True


project_github_link = 'https://github.com/pytorch/pytorch_sphinx_theme'

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

docs_root = os.path.abspath(os.path.dirname(__file__))
html_theme_path = [os.path.join(docs_root, '..', '_themes')]
html_theme = 'pytorch_sphinx_theme2'
html_static_path = ['_static']

html_css_files = [
    'css/bootstrap.min.css',
    'css/theme.css',
    'https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css'
]

html_js_files = [
   'js/bootstrap.min.js',
   'js/side-menus.js',

]

templates_path = ['_templates', '../_themes/pytorch_sphinx_theme2/templates']

navigation_links = [
    ('Home', 'index'),
    ('Tutorials', 'tutorials'),
]

theme_templates_path = os.path.join(html_theme_path[0], html_theme, 'templates')
templates_path = [theme_templates_path] + ['_templates']

html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_with_keys': True,
    'logo_only': False,
}

def process_docstring(app, what_, name, obj, options, lines):
    """
    Custom process to transform docstring lines Remove "Ignore" blocks

    Args:
        app (sphinx.application.Sphinx): the Sphinx application object

        what (str):
            the type of the object which the docstring belongs to (one of
            "module", "class", "exception", "function", "method", "attribute")

        name (str): the fully qualified name of the object

        obj: the object itself

        options: the options given to the directive: an object with
            attributes inherited_members, undoc_members, show_inheritance
            and noindex that are true if the flag option of same name was
            given to the auto directive

        lines (List[str]): the lines of the docstring, see above

    References:
        https://www.sphinx-doc.org/en/1.5.1/_modules/sphinx/ext/autodoc.html
        https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
    """
    import re

    remove_directives = [
        # Remove all xdoctest directives
        re.compile(r"\s*>>>\s*#\s*x?doctest:\s*.*"),
        re.compile(r"\s*>>>\s*#\s*x?doc:\s*.*"),
    ]
    filtered_lines = [
        line for line in lines if not any(pat.match(line) for pat in remove_directives)
    ]
    # Modify the lines inplace
    lines[:] = filtered_lines

    # make sure there is a blank line at the end
    if lines and lines[-1].strip():
        lines.append("")

from sphinx.writers import html, html5
from docutils import nodes
from sphinx import addnodes
from sphinx.util.docfields import TypedField

def replace(Klass):
    old_call = Klass.visit_reference

    def visit_reference(self, node):
        if "refuri" in node and "generated" in node.get("refuri"):
            ref = node.get("refuri")
            ref_anchor = ref.split("#")
            if len(ref_anchor) > 1:
                # Only add the id if the node href and the text match,
                # i.e. the href is "torch.flip#torch.flip" and the content is
                # "torch.flip" or "flip" since that is a signal the node refers
                # to autogenerated content
                anchor = ref_anchor[1]
                txt = node.parent.astext()
                if txt == anchor or txt == anchor.split(".")[-1]:
                    self.body.append(f'<p id="{ref_anchor[1]}"/>')
        return old_call(self, node)

    Klass.visit_reference = visit_reference


replace(html.HTMLTranslator)
replace(html5.HTML5Translator)

def setup(app):
    app.add_config_value('navigation_links', navigation_links, 'env')
    app.add_config_value('project_github_link', project_github_link, 'env')
    app.add_directive('autosummary', CustomAutosummary)
    # Function to add custom variables to the template context
    def add_custom_template_variables(app, pagename, templatename, context, doctree):
        context['navigation_links'] = app.config.navigation_links
        context['project_github_link'] = app.config.project_github_link
    # Connect the function to the html-page-context event
    app.connect("html-page-context", add_custom_template_variables)
    app.connect("autodoc-process-docstring", process_docstring)

def patched_make_field(self, types, domain, items, **kw):
    # `kw` catches `env=None` needed for newer sphinx while maintaining
    #  backwards compatibility when passed along further down!

    # type: (List, unicode, Tuple) -> nodes.field
    def handle_item(fieldarg, content):
        par = nodes.paragraph()
        par += addnodes.literal_strong("", fieldarg)  # Patch: this line added
        # par.extend(self.make_xrefs(self.rolename, domain, fieldarg,
        #                           addnodes.literal_strong))
        if fieldarg in types:
            par += nodes.Text(" (")
            # NOTE: using .pop() here to prevent a single type node to be
            # inserted twice into the doctree, which leads to
            # inconsistencies later when references are resolved
            fieldtype = types.pop(fieldarg)
            if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                typename = fieldtype[0].astext()
                builtin_types = ["int", "long", "float", "bool", "type"]
                for builtin_type in builtin_types:
                    pattern = rf"(?<![\w.]){builtin_type}(?![\w.])"
                    repl = f"python:{builtin_type}"
                    typename = re.sub(pattern, repl, typename)
                par.extend(
                    self.make_xrefs(
                        self.typerolename,
                        domain,
                        typename,
                        addnodes.literal_emphasis,
                        **kw,
                    )
                )
            else:
                par += fieldtype
            par += nodes.Text(")")
        par += nodes.Text(" -- ")
        par += content
        return par

    fieldname = nodes.field_name("", self.label)
    if len(items) == 1 and self.can_collapse:
        fieldarg, content = items[0]
        bodynode = handle_item(fieldarg, content)
    else:
        bodynode = self.list_type()
        for fieldarg, content in items:
            bodynode += nodes.list_item("", handle_item(fieldarg, content))
    fieldbody = nodes.field_body("", bodynode)
    return nodes.field("", fieldname, fieldbody)


TypedField.make_field = patched_make_field

copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True
