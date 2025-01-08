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

## Testing intersphinx:

* Here is test one `:func:`: {func}`torch.rand`, {func}`torch.rand_like`
* Here is test two `:class:`: {class}`torch.amp`
* Here is test three `:py:class:` : {py:class}`.DynamicRendezvousHandler`, {py:class}`torch.distributed.elastic.rendezvous.etcd_rendezvous_backend.EtcdRendezvousBackend`, :py:class:`RendezvousInfo`. Truncated version like `{py:class:}.EtcdRendezvousBackend` won't generate a link.
* Here is test four: `:py:mod:`: {py:mod}`torch.distributed.checkpoint.storage`
* Here is test five `:py:meth:`: {py:meth}`torch.distributed.state_dict_saver.save`, {py:meth}`torch.distributed.state_dict_loader.load` - these two examples are not valid because those functions are not part of a class, so the link is not generated. For functions like that `{func}` role should be used. 
* Here is test six: `:py:obj:`: {py:obj}`torch.nn.Module.apply`
* Here is test sever `:py:module:`: {py:module}`torch.amp` not valid 
* Here is another testi `:py:attr:`: {py:attr}`torch.nn.LazyConvTranspose3d.cls_to_become`

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
```
