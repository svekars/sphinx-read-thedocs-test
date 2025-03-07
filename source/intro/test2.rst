Test 2 page
============

torch.library is a collection of APIs for extending PyTorch's core library
of operators. It contains utilities for testing custom operators, creating new
custom operators, and extending operators defined with PyTorch's C++ operator
registration APIs (e.g. aten operators).

For a detailed guide on effectively using these APIs, please see
for more details on how to effectively use these APIs.

.. warning::
   The low-level operator registration APIs and the PyTorch Dispatcher are a
   complicated PyTorch concept. We recommend you use the higher level APIs above
   (that do not require a torch.library.Library object) when possible.
   This blog post <http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/>`_
   is a good starting point to learn about the PyTorch Dispatcher.

