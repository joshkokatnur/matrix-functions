# matrixfunctions

This is a test project that adds basic one and two dimensional matrix functionality to python.

## Matrix Class / Functions
**class Matrix(data)** - The matrix class that converts a list to a matrix and makes the data accessible by these functions.

**Matrix.shape()** - Returns the shape (rows x columns) of the matrix.

**def zeros(shape)** - Returns a matrix of the given shape, in which every element is 0.

**def ones(shape)** - Returns a matrix of the given shape, in which every element is 1.

**def reshape(mat, shape)** - Transforms the given matrix into the given shape.

**def transpose(mat)** - Transposes the given matrix.

**def flatten(data)** - Flattens a list into a single dimension.

**def add(mat1, mat2)** - Adds two matrices together element-wise.

**def subtract(mat1, mat2)** - Subtracts mat2 from mat1 element-wise.

**def multiply_elementwise(mat1, mat2)** - Multiplies two matrices together element-wise.

**def multiply_scalar(mat, value)** - Multiplies each element in the matrix by a given scalar value.

**def vector_dot_product(vec1, vec2)** - Calculates the dot product of two vectors (1-d matrices)

**def multiply(mat1, mat2)** - Performs matrix multiplication between mat1 and mat2.


## How to Install (from command-line)
Create a virtual python environement
```
$ python3 -m venv environment_name
```
Activate the environment
```
$ source environment_name/bin/activate
```
Install matrixfunctions
```
$ pip install -i https://test.pypi.org/simple/ matrixfunctions
```
Start a python interactive session
```
$ python3
```
Import matrixfunctions
```python
>>> from matrixfunctions.matrixfunctions import *
```
