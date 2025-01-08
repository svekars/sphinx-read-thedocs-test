Here's the Markdown conversion of the provided RST content:

# torch.nn

## Module Contents

- [torch.nn](#module-torch.nn)
- [torch.nn.modules](#module-torch.nn.modules)
- [Containers](#containers)
- [Global Hooks For Module](#global-hooks-for-module)
- [Convolution Layers](#convolution-layers)
- [Pooling layers](#pooling-layers)
- [Padding Layers](#padding-layers)
- [Non-linear Activations (weighted sum, nonlinearity)](#non-linear-activations-weighted-sum-nonlinearity)
- [Non-linear Activations (other)](#non-linear-activations-other)
- [Normalization Layers](#normalization-layers)
- [Recurrent Layers](#recurrent-layers)
- [Transformer Layers](#transformer-layers)
- [Linear Layers](#linear-layers)
- [Dropout Layers](#dropout-layers)
- [Sparse Layers](#sparse-layers)
- [Distance Functions](#distance-functions)
- [Loss Functions](#loss-functions)
- [Vision Layers](#vision-layers)
- [Shuffle Layers](#shuffle-layers)
- [DataParallel Layers (multi-GPU, distributed)](#dataparallel-layers-multi-gpu-distributed)
- [Utilities](#utilities)
- [Quantized Functions](#quantized-functions)
- [Lazy Modules Initialization](#lazy-modules-initialization)
- [Aliases](#aliases)

These are the basic building blocks for graphs:

## Containers

```python
class torch.nn.Module
class torch.nn.Sequential
class torch.nn.ModuleList
class torch.nn.ModuleDict
class torch.nn.ParameterList
class torch.nn.ParameterDict
```

## Global Hooks For Module

```python
torch.nn.modules.module.register_module_forward_pre_hook(hook)
torch.nn.modules.module.register_module_forward_hook(hook)
torch.nn.modules.module.register_module_backward_hook(hook)
torch.nn.modules.module.register_module_full_backward_pre_hook(hook)
torch.nn.modules.module.register_module_full_backward_hook(hook)
torch.nn.modules.module.register_module_buffer_registration_hook(hook)
torch.nn.modules.module.register_module_module_registration_hook(hook)
torch.nn.modules.module.register_module_parameter_registration_hook(hook)
```

## Convolution Layers

```python
class torch.nn.Conv1d
class torch.nn.Conv2d
class torch.nn.Conv3d
class torch.nn.ConvTranspose1d
class torch.nn.ConvTranspose2d
class torch.nn.ConvTranspose3d
class torch.nn.LazyConv1d
class torch.nn.LazyConv2d
class torch.nn.LazyConv3d
class torch.nn.LazyConvTranspose1d
class torch.nn.LazyConvTranspose2d
class torch.nn.LazyConvTranspose3d
class torch.nn.Unfold
class torch.nn.Fold
```

## Pooling layers

```python
class torch.nn.MaxPool1d
class torch.nn.MaxPool2d
class torch.nn.MaxPool3d
class torch.nn.MaxUnpool1d
class torch.nn.MaxUnpool2d
class torch.nn.MaxUnpool3d
class torch.nn.AvgPool1d
class torch.nn.AvgPool2d
class torch.nn.AvgPool3d
class torch.nn.FractionalMaxPool2d
class torch.nn.FractionalMaxPool3d
class torch.nn.LPPool1d
class torch.nn.LPPool2d
class torch.nn.LPPool3d
class torch.nn.AdaptiveMaxPool1d
class torch.nn.AdaptiveMaxPool2d
class torch.nn.AdaptiveMaxPool3d
class torch.nn.AdaptiveAvgPool1d
class torch.nn.AdaptiveAvgPool2d
class torch.nn.AdaptiveAvgPool3d
```

## Padding Layers

```python
class torch.nn.ReflectionPad1d
class torch.nn.ReflectionPad2d
class torch.nn.ReflectionPad3d
class torch.nn.ReplicationPad1d
class torch.nn.ReplicationPad2d
class torch.nn.ReplicationPad3d
class torch.nn.ZeroPad1d
class torch.nn.ZeroPad2d
class torch.nn.ZeroPad3d
class torch.nn.ConstantPad1d
class torch.nn.ConstantPad2d
class torch.nn.ConstantPad3d
class torch.nn.CircularPad1d
class torch.nn.CircularPad2d
class torch.nn.CircularPad3d
```

## Non-linear Activations (weighted sum, nonlinearity)

```python
class torch.nn.ELU
class torch.nn.Hardshrink
class torch.nn.Hardsigmoid
class torch.nn.Hardtanh
class torch.nn.Hardswish
class torch.nn.LeakyReLU
class torch.nn.LogSigmoid
class torch.nn.MultiheadAttention
class torch.nn.PReLU
class torch.nn.ReLU
class torch.nn.ReLU6
class torch.nn.RReLU
class torch.nn.SELU
class torch.nn.CELU
class torch.nn.GELU
class torch.nn.Sigmoid
class torch.nn.SiLU
class torch.nn.Mish
class torch.nn.Softplus
class torch.nn.Softshrink
class torch.nn.Softsign
class torch.nn.Tanh
class torch.nn.Tanhshrink
class torch.nn.Threshold
class torch.nn.GLU
```

## Non-linear Activations (other)

```python
class torch.nn.Softmin
class torch.nn.Softmax
class torch.nn.Softmax2d
class torch.nn.LogSoftmax
class torch.nn.AdaptiveLogSoftmaxWithLoss
```

## Normalization Layers

```python
class torch.nn.BatchNorm1d
class torch.nn.BatchNorm2d
class torch.nn.BatchNorm3d
class torch.nn.LazyBatchNorm1d
class torch.nn.LazyBatchNorm2d
class torch.nn.LazyBatchNorm3d
class torch.nn.GroupNorm
class torch.nn.SyncBatchNorm
class torch.nn.InstanceNorm1d
class torch.nn.InstanceNorm2d
class torch.nn.InstanceNorm3d
class torch.nn.LazyInstanceNorm1d
class torch.nn.LazyInstanceNorm2d
class torch.nn.LazyInstanceNorm3d
class torch.nn.LayerNorm
class torch.nn.LocalResponseNorm
class torch.nn.RMSNorm
```

## Recurrent Layers

```python
class torch.nn.RNNBase
class torch.nn.RNN
class torch.nn.LSTM
class torch.nn.GRU
class torch.nn.RNNCell
class torch.nn.LSTMCell
class torch.nn.GRUCell
```

## Transformer Layers

```python
class torch.nn.Transformer
class torch.nn.TransformerEncoder
class torch.nn.TransformerDecoder
class torch.nn.TransformerEncoderLayer
class torch.nn.TransformerDecoderLayer
```

## Linear Layers

```python
class torch.nn.Identity
class torch.nn.Linear
class torch.nn.Bilinear
class torch.nn.LazyLinear
```

## Dropout Layers

```python
class torch.nn.Dropout
class torch.nn.Dropout1d
class torch.nn.Dropout2d
class torch.nn.Dropout3d
class torch.nn.AlphaDropout
class torch.nn.FeatureAlphaDropout
```

## Sparse Layers

```python
class torch.nn.Embedding
class torch.nn.EmbeddingBag
```

## Distance Functions

```python
class torch.nn.CosineSimilarity
class torch.nn.PairwiseDistance
```

## Loss Functions

```python
class torch.nn.L1Loss
class torch.nn.MSELoss
class torch.nn.CrossEntropyLoss
class torch.nn.CTCLoss
class torch.nn.NLLLoss
class torch.nn.PoissonNLLLoss
class torch.nn.GaussianNLLLoss
class torch.nn.KLDivLoss
class torch.nn.BCELoss
class torch.nn.BCEWithLogitsLoss
class torch.nn.MarginRankingLoss
class torch.nn.HingeEmbeddingLoss
class torch.nn.MultiLabelMarginLoss
class torch.nn.HuberLoss
class torch.nn.SmoothL1Loss
class torch.nn.SoftMarginLoss
class torch.nn.MultiLabelSoftMarginLoss
class torch.nn.CosineEmbeddingLoss
class torch.nn.MultiMarginLoss
class torch.nn.TripletMarginLoss
class torch.nn.TripletMarginWithDistanceLoss
```

## Vision Layers

```python
class torch.nn.PixelShuffle
class torch.nn.PixelUnshuffle
class torch.nn.Upsample
class torch.nn.UpsamplingNearest2d
class torch.nn.UpsamplingBilinear2d
```

## Shuffle Layers

```python
class torch.nn.ChannelShuffle
```

## DataParallel Layers (multi-GPU, distributed)

```python
class torch.nn.DataParallel
class torch.nn.parallel.DistributedDataParallel
```

## Utilities

From the `torch.nn.utils` module:

Utility functions to clip parameter gradients.

```python
torch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0)
torch.nn.utils.clip_grad_norm(parameters, max_norm, norm_type=2.0)
torch.nn.utils.clip_grad_value_(parameters, clip_value)
```

Utility functions to flatten and unflatten Module parameters to and from a single vector.

```python
torch.nn.utils.parameters_to_vector(parameters)
torch.nn.utils.vector_to_parameters(vec, parameters)
```

Utility functions to fuse Modules with BatchNorm modules.

```python
torch.nn.utils.fuse_conv_bn_eval(conv, bn)
torch.nn.utils.fuse_conv_bn_weights(conv, bn)
torch.nn.utils.fuse_linear_bn_eval(linear, bn)
torch.nn.utils.fuse_linear_bn_weights(linear, bn)
```

Utility functions to convert Module parameter memory formats.

```python
torch.nn.utils.convert_conv2d_weight_memory_format(conv2d, memory_format)
torch.nn.utils.convert_conv3d_weight_memory_format(conv3d, memory_format)
```

Utility functions to apply and remove weight normalization from Module parameters.

```python
torch.nn.utils.weight_norm(module, name='weight', dim=0)
torch.nn.utils.remove_weight_norm(module, name='weight')
torch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)
torch.nn.utils.remove_spectral_norm(module, name='weight')
```

Utility functions for initializing Module parameters.

```python
torch.nn.utils.skip_init(module, name='weight')
```

Utility classes and functions for pruning Module parameters.

```python
class torch.nn.utils.prune.BasePruningMethod
class torch.nn.utils.prune.PruningContainer
class torch.nn.utils.prune.Identity
class torch.nn.utils.prune.RandomUnstructured
class torch.nn.utils.prune.L1Unstructured
class torch.nn.utils.prune.RandomStructured
class torch.nn.utils.prune.LnStructured
class torch.nn.utils.prune.CustomFromMask
torch.nn.utils.prune.identity(module, name)
torch.nn.utils.prune.random_unstructured(module, name, amount)
torch.nn.utils.prune.l1_unstructured(module, name, amount)
torch.nn.utils.prune.random_structured(module, name, amount, dim)
torch.nn.utils.prune.ln_structured(module, name, amount, n, dim)
torch.nn.utils.prune.global_unstructured(parameters, pruning_method)
torch.nn.utils.prune.custom_from_mask(module, name, mask)
torch.nn.utils.prune.remove(module, name)
torch.nn.utils.prune.is_pruned(module)
```

Parametrizations implemented using the new parametrization functionality in `torch.nn.utils.parameterize.register_parametrization`.

```python
torch.nn.utils.parametrizations.orthogonal(tensor, gain=1)
torch.nn.utils.parametrizations.weight_norm(tensor, dim=0)
torch.nn.utils.parametrizations.spectral_norm(tensor, n_power_iterations=1, dim=None)
```

Utility functions to parametrize Tensors on existing Modules. Note that these functions can be used to parametrize a given Parameter or Buffer given a specific function that maps from an input space to the parametrized space. They are not parameterizations that would transform an object into a parameter. See the [Parametrizations tutorial](https://pytorch.org/tutorials/intermediate/parametrizations.html) for more information on how to implement your own parametrizations.

```python
torch.nn.utils.parametrize.register_parametrization(parametrization, cls)
torch.nn.utils.parametrize.remove_parametrizations(module, parametrizations)
torch.nn.utils.parametrize.cached(module)
torch.nn.utils.parametrize.is_parametrized(module)
class torch.nn.utils.parametrize.ParametrizationList
```

Utility functions to call a given Module in a stateless manner.

```python
torch.nn.utils.stateless.functional_call(module, inputs, params=None)
```

Utility functions in other modules

```python
class torch.nn.utils.rnn.PackedSequence
torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)
torch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)
torch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)
torch.nn.utils.rnn.pack_sequence(sequences, enforce_sorted=True)
torch.nn.utils.rnn.unpack_sequence(sequence, batch_first=False)
torch.nn.utils.rnn.unpad_sequence(sequence, batch_first=False)

class torch.nn.Flatten
class torch.nn.Unflatten
```

## Quantized Functions

Quantization refers to techniques for performing computations and storing tensors at lower bitwidths than floating point precision. PyTorch supports both per tensor and per channel asymmetric linear quantization. To learn more how to use quantized functions in PyTorch, please refer to the [quantization documentation](https://pytorch.org/docs/stable/quantization.html).

## Lazy Modules Initialization

```python
class torch.nn.modules.lazy.LazyModuleMixin
```

## Aliases

The following are aliases to their counterparts in `torch.nn`:

```python
class torch.nn.modules.normalization.RMSNorm
```

Here's the Markdown version of the provided RST content:

### [torch.nn.utils.parametrize](https://pytorch.org/docs/stable/nn.utils.html#torch.nn.utils.parametrize)

```python
def parametrize(module, names=None):
    """Make a :class:`nn.Module` parametrized, such that its parameters can be
    accessed with Python attribute accesses instead of ``module.parameters()``.

    Args:
        module (nn.Module): The module to be parametrized
        names (list of str, optional): List of parameter names to be parametrized.
            If ``None``, all parameters will be parametrized.

    Example::

        >>> m = nn.Conv2d(3, 5, 2)
        >>> nn.utils.parametrize.parametrize(m)
        >>> m.weight  # Parametrized weight
        Parameter containing:
        tensor([[[[-0.0322, -0.0253],
                  [-0.0284, -0.0012],
                  [ 0.0272,  0.0286],
                  ...,
                  [ 0.0253, -0.0063],
                  [-0.0066, -0.0211],
                  [-0.0155,  0.0235]]],


                [[[...

    """
    ...
```

### [torch.nn.utils.prune](https://pytorch.org/docs/stable/nn.utils.html#torch.nn.utils.prune)

```python
def prune(module, name, amount=0.0, importance=None, importance_fn=None, force_pruning=False):
    """Prune the tensor corresponding to the parameter called `name` in the
    given module. The pruning is a permanent operation and cannot be undone.

    Args:
        module (nn.Module): The module containing the parameter to prune.
        name (str): The name of the parameter to prune.
        amount (float, optional): The fraction of weights to prune.
        importance (torch.Tensor, optional): The importance values used for ranking
            and pruning weights. If provided, `importance_fn` is ignored.
        importance_fn (callable, optional): A function that computes the importance
            values used for ranking and pruning weights. If provided, `importance`
            is ignored.
        force_pruning (bool, optional): Whether to force pruning even if the
            parameter is a view or was already pruned. This may cause
            inconsistencies in the pruned module's parameters, so use with
            caution.

    Returns:
        nn.Module: The pruned module.

    Example::

        >>> m = nn.Linear(10, 5)
        >>> nn.utils.prune.prune(m, 'weight', amount=0.5)
        >>> print(m.weight.shape)
        torch.Size([5, 5])

    """
    ...
```

### [torch.nn.utils.rnn](https://pytorch.org/docs/stable/nn.utils.html#torch.nn.utils.rnn)

```python
def pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True):
    """Packs a tensor containing padded sequences of varying lengths.

    ``input`` should contain padded sequences with size ``(T x B x *)``,
    where `T` is the length of the longest sequence, and `B` is the
    batch size. The sequences should be sorted by length in descending order,
    which is a requirement for use with ``pack_padded_sequence``.

    Upon successful execution, a ``PackedSequence`` object will be returned,
    containing data tensor ``(T' x B' x *)``, where `T'` is the sum of lengths
    of the sequences in the batch, and `B'` is the batch size. Lengths tensor
    ``(B')`` containing the lengths of each sequence in the batch will also be
    returned.

    Arguments:
        input (Tensor): padded batch of variable length sequences.
        lengths (Tensor): list of sequence lengths of each batch element.
        batch_first (bool, optional): if ``True``, the input is expected in
            ``(B, T, *)`` instead of ``(T, B, *)`` format. Default: ``False``.
        enforce_sorted (bool, optional): if ``True``, the input tensor is
            expected to contain sequences sorted by length in a descending
            order. If ``False``, the input will get sorted if it's not
            already sorted. Default: ``True``.

    Returns:
        A ``PackedSequence`` object with useful views into the data.

    Example:
        >>> from torch.nn.utils.rnn import pack_padded_sequence
        >>> data = torch.tensor([[[1, 2], [3, 3]], [[1, 5], [7, 9]]])
        >>> lengths = torch.tensor([2, 2])
        >>> packed = pack_padded_sequence(data, lengths, batch_first=True)
        >>> packed.data.shape
        torch.Size([4, 2, 2])
        >>> packed.batch_sizes
        tensor([2, 2])
        >>> packed.sorted_indices
        tensor([0, 1])
        >>> packed.unsorted_indices
        tensor([0, 1])

    """
    ...

def pack_sequence(sequences, enforce_sorted=True):
    """Packs a list of tensors by concatenating sequences along the first dimension,
    and providing the lengths of each tensor as a list of integers.

    Arguments:
        sequences (list[Tensor]): list of sequences to be padded.
        enforce_sorted (bool, optional): if ``True``, the input tensors are
            expected to be sorted by length in a descending order. If ``False``,
            the input will get sorted if it's not already sorted. Default: ``True``.

    Returns:
        A ``PackedSequence`` object with useful views into the data.

    Example:
        >>> from torch.nn.utils.rnn import pack_sequence
        >>> data = [torch.tensor([1, 2, 3]), torch.tensor([1, 2]), torch.tensor([1])]
        >>> packed = pack_sequence(data)
        >>> packed.data.shape
        torch.Size([6, 1])
        >>> packed.batch_sizes
        tensor([3, 2, 1])
        >>> packed.sorted_indices
        tensor([2, 1, 0])
        >>> packed.unsorted_indices
        tensor([2, 0, 1])

    """
    ...

def pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None):
    """Pads a packed batch of variable length sequences.

    It is an inverse operation to :func:`pack_padded_sequence`.

    The returned Tensor's data will have the format ``(T x B x *)`` if ``batch_first=False``
    or ``(B x T x *)`` if ``batch_first=True``, where `T` is the length of the
    longest sequence, and `B` is the batch size. The data will have its
    padded elements set to ``padding_value``.

    ``total_length`` is the length of the longest sequence in the batch after padding.
    If ``total_length`` is not provided, it will be calculated by
    ``max_sequence_length + 2``, where ``max_sequence_length`` is the length of the
    longest sequence in the batch.

    ``total_length`` is useful for cases where the sequences are
    further padded before being passed to the encoder/decoder of an RNN. For
    example, in machine translation, each sequence may be padded
    ``sos_id .... eos_id`` before being passed to an encoder.

    ``padding_value`` is the value to be used for padding missing entries in the data.
    ``padding_value=0.0`` is used for NLP models and ``padding_value=0`` is used for
    vision models.

    ``batch_first`` is a boolean indicating if the data is batched by the batch
    dimension (``batch_first=True``) or the sequence dimension
    (``batch_first=False``). ``batch_first=True`` is useful for RNN models
    that take the batch dimension first, while ``batch_first=False`` is an
    efficient data format for LSTM models that take the sequence dimension
    first.

    Args:
        sequence (PackedSequence): A packed batch of variable length sequences.
        batch_first (bool, optional): if ``True``, the output will be in
            ``B x T x *`` format.
        padding_value (float, optional): values for padded elements.
        total_length (int, optional): if not provided, it will be calculated
            to be the length of the longest sequence in the batch.

    Returns:
        Tuple of Tensor, Tensor: The padded data tensor and the list of sequence lengths.

    Example:
        >>> from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
        >>> data = torch.tensor([[[1, 2], [3, 3]], [[1, 5], [7, 9]]])
        >>> lengths = torch.tensor([2, 2])
        >>> packed = pack_padded_sequence(data, lengths, batch_first=True)
        >>> padded, lengths = pad_packed_sequence(packed, batch_first=True)
        >>> padded.shape
        torch.Size([2, 2, 2])
        >>> lengths
        tensor([2, 2])

    """
    ...

def pad_sequence(sequences, batch_first=False, padding_value=0):
    r"""Pad a list of variable length Tensors with ``padding_value``

    ``pad_sequence`` stacks a list of Tensors along a new dimension,
    and pads them to equal length. For example, if the input is list of
    sequences with size ``L x *`` and if batch_first is False, and ``T x B x *``
    otherwise.

    `B` is batch size. It is equal to the number of elements in ``sequences``.
    `T` is length of the longest sequence.
    `L` is length of the sequence.
    `*` is any number of trailing dimensions, including none.

    Example:
        >>> from torch.nn.utils.rnn import pad_sequence
        >>> a = torch.ones(25, 300)
        >>> b = torch.ones(22, 300)
        >>> c = torch.ones(15, 300)
        >>> pad_sequence([a, b, c]).size()
        torch.Size([25, 3, 300])

    Note:
        This function returns a Tensor of size ``T x B x *`` or ``B x T x *``
        where `T` is the length of the longest sequence. This function assumes
        trailing dimensions and type of all the Tensors in sequences are same.

    Arguments:
        sequences (list[Tensor]): list of variable length sequences.
        batch_first (bool, optional): output will be in ``B x T x *`` if True, or in
            ``T x B x *`` otherwise
        padding_value (float, optional): value for padded elements. Default: 0.

    Returns:
        Tensor of size ``T x B x *`` if :attr:`batch_first` is ``False``.
        Tensor of size ``B x T x *`` otherwise
    """
    ...

def pack_sequence_batch(sequences, batch_first=False, enforce_sorted=True):
    """Packs a list of tensors into a PackedSequenceBatch object.

    This function is a convenience wrapper around :func:`pack_sequence` and
    :func:`pack_padded_sequence` that allows packing a list of tensors into a
    PackedSequenceBatch object, which can be used as input to a
    :class:`~torch.nn.utils.rnn.PackedSequence` module.

    Arguments:
        sequences (list[Tensor]): A list of tensors to be packed.
        batch_first (bool, optional): If ``True``, the input tensors are expected
            to be of shape ``(B, T, *)``, where `B` is the batch size and `T` is
            the sequence length. If ``False``, the input tensors are expected to
            be of shape ``(T, B, *)``. Default: ``False``.
        enforce_sorted (bool, optional): If ``True``, the input tensors are
            expected to be sorted by length in descending order. If ``False``,
            the input will get sorted if it's not already sorted. Default: ``True``.

    Returns:
        A :class:`~torch.nn.utils.rnn.PackedSequenceBatch` object containing the
        packed sequences and their lengths.

    Example:
        >>> from torch.nn.utils.rnn import pack_sequence_batch
        >>> data = [torch.tensor([1, 2, 3]), torch.tensor([1, 2]), torch.tensor([1])]
        >>> packed = pack_sequence_batch(data)
        >>> packed.data.shape
        torch.Size([6, 1])
        >>> packed.batch_sizes
        tensor([3, 2, 1])
        >>> packed.sorted_indices
        tensor([2, 1, 0])
        >>> packed.unsorted_indices
        tensor([2, 0, 1])
    """
    ...

def pad_packed_sequence_batch(sequence_batch, batch_first=False, padding_value=0.0, total_length=None):
    """Pads a packed batch of variable length sequences.

    This function is a convenience wrapper around :func:`pad_packed_sequence`
    that allows padding a :class:`~torch.nn.utils.rnn.PackedSequenceBatch`
    object.

    Arguments:
        sequence_batch (PackedSequenceBatch): A packed batch of variable length
            sequences to be padded.
        batch_first (bool, optional): If ``True``, the output will be in
            ``B x T x *`` format. If ``False``, the output will be in
            ``T x B x *`` format. Default: ``False``.
        padding_value (float, optional): Value to use for padding. Default: 0.0.
        total_length (int, optional): If provided, the output will be padded to
            have this length. If not provided, the output will be padded to have
            the length of the longest sequence in the batch. Default: ``None``.

    Returns:
        Tuple of Tensor, Tensor: The padded data tensor and the list of sequence
        lengths.

    Example:
        >>> from torch.nn.utils.rnn import pack_sequence_batch, pad_packed_sequence_batch
        >>> data = [torch.tensor([1, 2, 3]), torch.tensor([1, 2]), torch.tensor([1])]
        >>> packed = pack_sequence_batch(data)
        >>> padded, lengths = pad_packed_sequence_batch(packed)
        >>> padded.shape
        torch.Size([3, 3, 1])
        >>> lengths
        tensor([3, 2, 1])
    """
    ...
```