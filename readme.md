loltree: convert list-of-lists to tree objects
==============================================

Having parsed (e.g.) lisp code into list-of-lists format, libraries for
interacting with this data may require that it be in the form of some
kind of object. This package converts list-of-lists into those
objects.

Currently, there is only one conversion, `zsstree`, which converts to
the tree objects used by https://github.com/timtadh/zhang-shasha.

Of course, that library itself is modular w/r/t the type of tree used,
but since I didn't have some other tree I desparately wanted to use
for this project, it was fine.

usage
-----

```python
from loltree import zsstree
from zss import simple_distance

A = zsstree(list_of_lists_A)
B = zsstree(list_of_lists_B)
simple_distance(A, B)
```

TODO
----

replace `src/loltree` with `loltree`; I now understand all the downsides
