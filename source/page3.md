# Test Markdown Page

Just testing a markdown page

This is markdown:

```python
import torch
# Create a 1D tensor (vector)
tensor_1d = torch.tensor([1, 2, 3, 4, 5])
print("1D Tensor:")
print(tensor_1d)
```

## Testing warning: 

```{warning}
Here's my admonition content
```

## API test

## Torch

```{eval-rst}
.. automodule:: torch
```

```{eval-rst}
.. currentmodule:: torch
```

### Tensors

```{eval-rst}
.. autosummary::
   :toctree: generated
   :nosignatures:

    is_tensor
    is_storage
    is_complex
    is_conj
    is_floating_point
    is_nonzero
    set_default_dtype
    get_default_dtype
    set_default_device
    get_default_device
    set_default_tensor_type
    numel
    set_printoptions
    set_flush_denormal
