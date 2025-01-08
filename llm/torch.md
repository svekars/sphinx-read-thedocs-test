Here's the Markdown version of the provided RST content:

# torch

## Tensors

### Creation Ops

> **Note:** Random sampling creation ops are listed under [Random sampling](#random-sampling) and include:
> - [`torch.rand`](https://pytorch.org/docs/stable/generated/torch.rand.html)
> - [`torch.rand_like`](https://pytorch.org/docs/stable/generated/torch.rand_like.html)
> - [`torch.randn`](https://pytorch.org/docs/stable/generated/torch.randn.html)
> - [`torch.randn_like`](https://pytorch.org/docs/stable/generated/torch.randn_like.html)
> - [`torch.randint`](https://pytorch.org/docs/stable/generated/torch.randint.html)
> - [`torch.randint_like`](https://pytorch.org/docs/stable/generated/torch.randint_like.html)
> - [`torch.randperm`](https://pytorch.org/docs/stable/generated/torch.randperm.html)
>
> You may also use [`torch.empty`](https://pytorch.org/docs/stable/generated/torch.empty.html) with the [in-place random sampling](#inplace-random-sampling) methods to create `torch.Tensor`s with values sampled from a broader range of distributions.

```python
import torch

# Example usage of torch.empty and in-place random sampling
x = torch.empty(5, 3)
x.normal_()
print(x)
```

[tensor([[ 0.4963, -0.6365,  0.2953],
         [-0.1422,  1.0829, -0.0257],
         [ 1.1089, -1.2099,  0.4294],
         [-0.2726, -0.4711,  0.7147],
         [ 0.0818, -0.6182,  0.1192]])]

- [`tensor`](https://pytorch.org/docs/stable/generated/torch.tensor.html)
- [`sparse_coo_tensor`](https://pytorch.org/docs/stable/generated/torch.sparse_coo_tensor.html)
- [`sparse_csr_tensor`](https://pytorch.org/docs/stable/generated/torch.sparse_csr_tensor.html)
- [`sparse_csc_tensor`](https://pytorch.org/docs/stable/generated/torch.sparse_csc_tensor.html)
- [`sparse_bsr_tensor`](https://pytorch.org/docs/stable/generated/torch.sparse_bsr_tensor.html)
- [`sparse_bsc_tensor`](https://pytorch.org/docs/stable/generated/torch.sparse_bsc_tensor.html)
- [`asarray`](https://pytorch.org/docs/stable/generated/torch.asarray.html)
- [`as_tensor`](https://pytorch.org/docs/stable/generated/torch.as_tensor.html)
- [`as_strided`](https://pytorch.org/docs/stable/generated/torch.as_strided.html)
- [`from_file`](https://pytorch.org/docs/stable/generated/torch.from_file.html)
- [`from_numpy`](https://pytorch.org/docs/stable/generated/torch.from_numpy.html)
- [`from_dlpack`](https://pytorch.org/docs/stable/generated/torch.from_dlpack.html)
- [`frombuffer`](https://pytorch.org/docs/stable/generated/torch.frombuffer.html)
- [`zeros`](https://pytorch.org/docs/stable/generated/torch.zeros.html)
- [`zeros_like`](https://pytorch.org/docs/stable/generated/torch.zeros_like.html)
- [`ones`](https://pytorch.org/docs/stable/generated/torch.ones.html)
- [`ones_like`](https://pytorch.org/docs/stable/generated/torch.ones_like.html)
- [`arange`](https://pytorch.org/docs/stable/generated/torch.arange.html)
- [`range`](https://pytorch.org/docs/stable/generated/torch.range.html)
- [`linspace`](https://pytorch.org/docs/stable/generated/torch.linspace.html)
- [`logspace`](https://pytorch.org/docs/stable/generated/torch.logspace.html)
- [`eye`](https://pytorch.org/docs/stable/generated/torch.eye.html)
- [`empty`](https://pytorch.org/docs/stable/generated/torch.empty.html)
- [`empty_like`](https://pytorch.org/docs/stable/generated/torch.empty_like.html)
- [`empty_strided`](https://pytorch.org/docs/stable/generated/torch.empty_strided.html)
- [`full`](https://pytorch.org/docs/stable/generated/torch.full.html)
- [`full_like`](https://pytorch.org/docs/stable/generated/torch.full_like.html)
- [`quantize_per_tensor`](https://pytorch.org/docs/stable/generated/torch.quantize_per_tensor.html)
- [`quantize_per_channel`](https://pytorch.org/docs/stable/generated/torch.quantize_per_channel.html)
- [`dequantize`](https://pytorch.org/docs/stable/generated/torch.dequantize.html)
- [`complex`](https://pytorch.org/docs/stable/generated/torch.complex.html)
- [`polar`](https://pytorch.org/docs/stable/generated/torch.polar.html)
- [`heaviside`](https://pytorch.org/docs/stable/generated/torch.heaviside.html)

### Indexing, Slicing, Joining, Mutating Ops

- [`adjoint`](https://pytorch.org/docs/stable/generated/torch.adjoint.html)
- [`argwhere`](https://pytorch.org/docs/stable/generated/torch.argwhere.html)
- [`cat`](https://pytorch.org/docs/stable/generated/torch.cat.html)
- [`concat`](https://pytorch.org/docs/stable/generated/torch.concat.html)
- [`concatenate`](https://pytorch.org/docs/stable/generated/torch.concatenate.html)
- [`conj`](https://pytorch.org/docs/stable/generated/torch.conj.html)
- [`chunk`](https://pytorch.org/docs/stable/generated/torch.chunk.html)
- [`dsplit`](https://pytorch.org/docs/stable/generated/torch.dsplit.html)
- [`column_stack`](https://pytorch.org/docs/stable/generated/torch.column_stack.html)
- [`dstack`](https://pytorch.org/docs/stable/generated/torch.dstack.html)
- [`gather`](https://pytorch.org/docs/stable/generated/torch.gather.html)
- [`hsplit`](https://pytorch.org/docs/stable/generated/torch.hsplit.html)
- [`hstack`](https://pytorch.org/docs/stable/generated/torch.hstack.html)
- [`index_add`](https://pytorch.org/docs/stable/generated/torch.index_add.html)
- [`index_copy`](https://pytorch.org/docs/stable/generated/torch.index_copy.html)
- [`index_reduce`](https://pytorch.org/docs/stable/generated/torch.index_reduce.html)
- [`index_select`](https://pytorch.org/docs/stable/generated/torch.index_select.html)
- [`masked_select`](https://pytorch.org/docs/stable/generated/torch.masked_select.html)
- [`movedim`](https://pytorch.org/docs/stable/generated/torch.movedim.html)
- [`moveaxis`](https://pytorch.org/docs/stable/generated/torch.moveaxis.html)
- [`narrow`](https://pytorch.org/docs/stable/generated/torch.narrow.html)
- [`narrow_copy`](https://pytorch.org/docs/stable/generated/torch.narrow_copy.html)
- [`nonzero`](https://pytorch.org/docs/stable/generated/torch.nonzero.html)
- [`permute`](https://pytorch.org/docs/stable/generated/torch.permute.html)
- [`reshape`](https://pytorch.org/docs/stable/generated/torch.reshape.html)
- [`row_stack`](https://pytorch.org/docs/stable/generated/torch.row_stack.html)
- [`select`](https://pytorch.org/docs/stable/generated/torch.select.html)
- [`scatter`](https://pytorch.org/docs/stable/generated/torch.scatter.html)
- [`diagonal_scatter`](https://pytorch.org/docs/stable/generated/torch.diagonal_scatter.html)
- [`select_scatter`](https://pytorch.org/docs/stable/generated/torch.select_scatter.html)
- [`slice_scatter`](https://pytorch.org/docs/stable/generated/torch.slice_scatter.html)
- [`scatter_add`](https://pytorch.org/docs/stable/generated/torch.scatter_add.html)
- [`scatter_reduce`](https://pytorch.org/docs/stable/generated/torch.scatter_reduce.html)
- [`split`](https://pytorch.org/docs/stable/generated/torch.split.html)
- [`squeeze`](https://pytorch.org/docs/stable/generated/torch.squeeze.html)
- [`stack`](https://pytorch.org/docs/stable/generated/torch.stack.html)
- [`swapaxes`](https://pytorch.org/docs/stable/generated/torch.swapaxes.html)
- [`swapdims`](https://pytorch.org/docs/stable/generated/torch.swapdims.html)
- [`t`](https://pytorch.org/docs/stable/generated/torch.t.html)
- [`take`](https://pytorch.org/docs/stable/generated/torch.take.html)
- [`take_along_dim`](https://pytorch.org/docs/stable/generated/torch.take_along_dim.html)
- [`tensor_split`](https://pytorch.org/docs/stable/generated/torch.tensor_split.html)
- [`tile`](https://pytorch.org/docs/stable/generated/torch.tile.html)
- [`transpose`](https://pytorch.org/docs/stable/generated/torch.transpose.html)
- [`unbind`](https://pytorch.org/docs/stable/generated/torch.unbind.html)
- [`unravel_index`](https://pytorch.org/docs/stable/generated/torch.unravel_index.html)
- [`unsqueeze`](https://pytorch.org/docs/stable/generated/torch.unsqueeze.html)
- [`vsplit`](https://pytorch.org/docs/stable/generated/torch.vsplit.html)
- [`vstack`](https://pytorch.org/docs/stable/generated/torch.vstack.html)
- [`where`](https://pytorch.org/docs/stable/generated/torch.where.html)

## Accelerators

Within the PyTorch repo, we define an "Accelerator" as a `torch.device` that is being used alongside a CPU to speed up computation. These devices use an asynchronous execution scheme, using `torch.Stream` and `torch.Event` as their main way to perform synchronization. We also assume that only one such accelerator can be available at once on a given host. This allows us to use the current accelerator as the default device for relevant concepts such as pinned memory, Stream device_type, FSDP, etc.

As of today, accelerator devices are (in no particular order) ["CUDA"](https://pytorch.org/docs/stable/cuda.html), ["MTIA"](https://pytorch.org/docs/stable/mtia.html), ["XPU"](https://pytorch.org/docs/stable/xpu.html), and PrivateUse1 (many devices not in the PyTorch repo itself).

- [`Stream`](https://pytorch.org/docs/stable/generated/torch.Stream.html)
- [`Event`](https://pytorch.org/docs/stable/generated/torch.Event.html)

## Generators

- [`Generator`](https://pytorch.org/docs/stable/generated/torch.Generator.html)

## Random sampling

- [`seed`](https://pytorch.org/docs/stable/generated/torch.seed.html)
- [`manual_seed`](https://pytorch.org/docs/stable/generated/torch.manual_seed.html)
- [`initial_seed`](https://pytorch.org/docs/stable/generated/torch.initial_seed.html)
- [`get_rng_state`](https://pytorch.org/docs/stable/generated/torch.get_rng_state.html)
- [`set_rng_state`](https://pytorch.org/docs/stable/generated/torch.set_rng_state.html)

`torch.default_generator` returns the default CPU `torch.Generator`.

- [`bernoulli`](https://pytorch.org/docs/stable/generated/torch.bernoulli.html)
- [`multinomial`](https://pytorch.org/docs/stable/generated/torch.multinomial.html)
- [`normal`](https://pytorch.org/docs/stable/generated/torch.normal.html)
- [`poisson`](https://pytorch.org/docs/stable/generated/torch.poisson.html)
- [`rand`](https://pytorch.org/docs/stable/generated/torch.rand.html)
- [`rand_like`](https://pytorch.org/docs/stable/generated/torch.rand_like.html)
- [`randint`](https://pytorch.org/docs/stable/generated/torch.randint.html)
- [`randint_like`](https://pytorch.org/docs/stable/generated/torch.randint_like.html)
- [`randn`](https://pytorch.org/docs/stable/generated/torch.randn.html)
- [`randn_like`](https://pytorch.org/docs/stable/generated/torch.randn_like.html)
- [`randperm`](https://pytorch.org/docs/stable/generated/torch.randperm.html)

### In-place random sampling

There are a few more in-place random sampling functions defined on Tensors as well. Click through to refer to their documentation:

- [`torch.Tensor.bernoulli_`](https://pytorch.org/docs/stable/generated/torch.Tensor.bernoulli_.html) - in-place version of `torch.bernoulli`
- [`torch.Tensor.cauchy_`](https://pytorch.org/docs/stable/generated/torch.Tensor.cauchy_.html) - numbers drawn from the Cauchy distribution
- [`torch.Tensor.exponential_`](https://pytorch.org/docs/stable/generated/torch.Tensor.exponential_.html) - numbers drawn from the exponential distribution
- [`torch.Tensor.geometric_`](https://pytorch.org/docs/stable/generated/torch.Tensor.geometric_.html) - elements drawn from the geometric distribution
- [`torch.Tensor.log_normal_`](https://pytorch.org/docs/stable/generated/torch.Tensor.log_normal_.html) - samples from the log-normal distribution
- [`torch.Tensor.normal_`](https://pytorch.org/docs/stable/generated/torch.Tensor.normal_.html) - in-place version of `torch.normal`
- [`torch.Tensor.random_`](https://pytorch.org/docs/stable/generated/torch.Tensor.random_.html) - numbers sampled from the discrete uniform distribution
- [`torch.Tensor.uniform_`](https://pytorch.org/docs/stable/generated/torch.Tensor.uniform_.html) - numbers sampled from the continuous uniform distribution

### Quasi-random sampling

- [`quasirandom.SobolEngine`](https://pytorch.org/docs/stable/generated/torch.quasirandom.SobolEngine.html)

## Serialization

- [`save`](https://pytorch.org/docs/stable/generated/torch.save.html)
- [`load`](https://pytorch.org/docs/stable/generated/torch.load.html)

## Parallelism

- [`get_num_threads`](https://pytorch.org/docs/stable/generated/torch.get_num_threads.html)
- [`set_num_threads`](https://pytorch.org/docs/stable/generated/torch.set_num_threads.html)
- [`get_num_interop_threads`](https://pytorch.org/docs/stable/generated/torch

Here's the Markdown version of the provided RST content:

# get_device_module
# is_warn_always_enabled
# vmap
# _assert

## Symbolic Numbers

### SymInt

```python
class SymInt:
    """Symbolic Integer class documentation goes here."""
    def __init__(self):
        pass

    def method1(self):
        """Method 1 documentation."""
        pass

    def method2(self):
        """Method 2 documentation."""
        pass
```

### SymFloat

```python
class SymFloat:
    """Symbolic Float class documentation goes here."""
    def __init__(self):
        pass

    def method1(self):
        """Method 1 documentation."""
        pass

    def method2(self):
        """Method 2 documentation."""
        pass
```

### SymBool

```python
class SymBool:
    """Symbolic Boolean class documentation goes here."""
    def __init__(self):
        pass

    def method1(self):
        """Method 1 documentation."""
        pass

    def method2(self):
        """Method 2 documentation."""
        pass
```

- [sym_float](generated/sym_float.md)
- [sym_int](generated/sym_int.md)
- [sym_max](generated/sym_max.md)
- [sym_min](generated/sym_min.md)
- [sym_not](generated/sym_not.md)
- [sym_ite](generated/sym_ite.md)

## Export Path

> **Warning**
> This feature is a prototype and may have compatibility breaking changes in the future.

- [export](generated/export.md)
- [generated/exportdb/index](generated/exportdb/index.md)

## Control Flow

> **Warning**
> This feature is a prototype and may have compatibility breaking changes in the future.

- [cond](generated/cond.md)

## Optimizations

- [compile](generated/compile.md)

[torch.compile documentation](https://pytorch.org/docs/main/torch.compiler.html)

## Operator Tags

### Tag

```python
class Tag:
    """Tag class documentation goes here."""
    def __init__(self):
        pass

    def method1(self):
        """Method 1 documentation."""
        pass

    def method2(self):
        """Method 2 documentation."""
        pass
```

```python
# Empty submodules added only for tracking.
import torch.contrib
import torch.utils.backcompat
import torch.utils.hipify  # This module is only used internally for ROCm builds.
import torch.utils.model_dump  # This module needs to be documented.
import torch.utils.viz
import torch.functional
import torch.quasirandom
import torch.return_types
import torch.serialization
import torch.signal.windows.windows
import torch.sparse.semi_structured
import torch.storage
import torch.torch_version
import torch.types
import torch.version
```