# NumPy Technical README

Welcome to the technical README for NumPy. This document provides a concise overview of the core features, documentation usage, available subpackages, and essential utilities for developers and advanced users.

---

## Core Features

1. **Array Object**  
   Efficient, homogeneous, N-dimensional array objects for numerical data.

2. **Fast Mathematical Operations**  
   High-performance mathematical functions operating over entire arrays.

3. **Advanced Modules**  
   - Linear Algebra
   - Fourier Transforms
   - Random Number Generation

---

## How to Use the Documentation

NumPy documentation is available in two forms:
- **Docstrings**: Embedded within the code for quick reference.
- **Reference Guide**: Comprehensive documentation at the [NumPy homepage](https://numpy.org).

We recommend exploring docstrings interactively using [IPython](https://ipython.org), which offers TAB-completion and introspection.

### Example Usage

Import NumPy as `np`:

```python
import numpy as np
```

Code snippets are indicated by three greater-than signs:

```python
>>> x = 42
>>> x = x + 1
```

To view a function's docstring, use the built-in `help` function:

```python
>>> help(np.sort)
# doctest: +SKIP
```

For certain objects, `np.info(obj)` may provide additional help, especially for ufuncs (universal functions) implemented in C.

---

## Available Subpackages

| Subpackage   | Description                                      |
|--------------|--------------------------------------------------|
| `lib`        | Basic functions used by several sub-packages     |
| `random`     | Core random number generation tools              |
| `linalg`     | Core linear algebra tools                        |
| `fft`        | Core FFT routines                                |
| `polynomial` | Polynomial tools                                 |
| `testing`    | NumPy testing tools                              |
| `distutils`  | Distutils enhancements (Fortran support, <=3.11) |

---

## Utilities

- `test`         : Run NumPy unittests
- `show_config`  : Show NumPy build configuration
- `__version__`  : NumPy version string

---

## Viewing Documentation in IPython

Start IPython and import NumPy (usually as `np`):

```python
import numpy as np
```

- Use `np.<TAB>` to see available functions.
- Use `np.*cos*?` to search for functions containing "cos".
- Use `np.cos?` to view a function's docstring.
- Use `np.cos??` to view the source code.

---

## Copies vs. In-Place Operations

Most NumPy functions return a copy of the array argument (e.g., `np.sort`).  
In-place versions are often available as array methods:

```python
x = np.array([1, 2, 3])
x.sort()  # In-place sort
```

Exceptions to this rule are documented in the respective function docstrings.

---
