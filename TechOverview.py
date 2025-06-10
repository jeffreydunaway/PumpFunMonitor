##Technical Overview of NumPy##
"""

NumPy Technical Overview
========================

-------------
1. Array object of arbitrary homogeneous items.
2. Fast mathematical operations over arrays.
3. Advanced modules: Linear Algebra, Fourier Transforms, Random Number Generation.

Documentation
-------------
- Docstrings are available within the code.
- A comprehensive reference guide is available at https://numpy.org.

We recommend using IPython (https://ipython.org) for interactive exploration with TAB-completion and introspection.

Example Usage:
    >>> import numpy as np
    >>> x = 42
    >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring:
    >>> help(np.sort)
    ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help, especially for ufuncs.

Available Subpackages
---------------------
- lib        : Basic functions used by several sub-packages.
- random     : Core random number tools.
- linalg     : Core linear algebra tools.
- fft        : Core FFT routines.
- polynomial : Polynomial tools.
- testing    : NumPy testing tools.
- distutils  : Distutils enhancements (Fortran support, Python <= 3.11).

Utilities
---------
- test         : Run NumPy unittests.
- show_config  : Show NumPy build configuration.
- __version__  : NumPy version string.

Viewing Documentation in IPython
--------------------------------
- Use ``np.<TAB>`` to see available functions.
- Use ``np.*cos*?`` to search for functions containing "cos".
- Use ``np.cos?`` to view a function's docstring.
- Use ``np.cos??`` to view the source code.

Copies vs. In-Place Operations
------------------------------
Most functions return a copy of the array argument (e.g., ``np.sort``).
In-place versions are often available as array methods:
    x = np.array([1, 2, 3])
    x.sort()  # In-place sort

Exceptions are documented in the respective function docstrings.
"""

import os
import sys
import warnings

from ._globals import _NoValue, _CopyMode
from ._expired_attrs_2_0 import __expired_attributes__

from . import version
from .version import __version__

# Detect if being called as part of the numpy setup procedure
try:
    __NUMPY_SETUP__
except NameError:
    __NUMPY_SETUP__ = False

if __NUMPY_SETUP__:
    sys.stderr.write('Running from numpy source directory.\n')
else:
    # Allow distributors to run custom init code before importing numpy._core
    from . import _distributor_init

    try:
        from numpy.__config__ import show_config
    except ImportError as e:
        msg = (
            "Error importing numpy: you should not try to import numpy from "
            "its source directory; please exit the numpy source tree, and relaunch "
            "your python interpreter from there."
        )
        raise ImportError(msg) from e

    # ...rest of the initialization code...
