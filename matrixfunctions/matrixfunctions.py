"""
The following class and functions add basic matrix functionality to python, similar to what other libraries such as NumPy and PyTorch add. 
It should be noted that these functions are only compatible with one and two dimensional matrices.
"""

class Matrix:
    def __init__(self, data):
        """ Initializes a matrix object.

        Args:
            data (list): Contains the numerical data for the matrix. Should be a list.
        """
        list_1d = flatten(data)
        if self.__dataIsNumerical(list_1d) and self.__shapeIsValid(data):
            self.data = data

    def __dataIsNumerical(self, list_1d):
        """ Checks that the list data is only numbers.

        Args:
            list_1d (list): The flattened (1-dimensional) list.
        Returns:
            bool: True if all elements are int or float. Raises TypeError otherwise.
        """
        if all(isinstance(x, (int, float)) for x in list_1d):
            return True
        else:
            raise TypeError('List elements should be of type int or float!')

    def __shapeIsValid(self, data):
        """ Checks that the list data can be converted to an n x m matrix (it checks that each row is the same length.)

        Args:
            data (list): The data that was passed at the initialization of the matrix.
        Returns:
            bool: True if the shape is valid. Raises ValueError otherwise. 
        """
        if hasattr(data[0], "__iter__"): # Checks if the first element of data is also a list
            initial_row_length = len(data[0])
            num_rows = len(data)
            if all(len(x)==initial_row_length for x in data):
                return True
            else:
                raise ValueError('All matrix rows should be the same length!')
        else:
            if any(hasattr(x, "__iter__") for x in data):
                raise ValueError('All matrix rows should be the same length!')
            else:
                return True

    def shape(self):
        """ Gets the shape of the matrix.

        Returns:
            tuple: The first element is the number of rows and the second element is the number of columns.
        """
        if hasattr(self.data[0], "__iter__"):
            num_rows = len(self.data)
            num_columns = len(self.data[0])
            if num_columns == 1:
                return (num_rows, 1)
            else:
                return (num_rows, num_columns)
        else:
            return (1, len(self.data))

    def __str__(self):
        """ Provides the format for printing the matrix.

        Returns:
            string: Each matrix row is printed on a new line.
        """
        text = ""
        
        if hasattr(self.data[0], "__iter__"):
            for row in self.data:
                text+=str(row)+"\n"
        else:
            text+=str(self.data)

        return text

    def __len__(self):
        """ Gets total number of elements in matrix.

        Returns:
            int: The total number of elements in the matrix.
        """
        return len(self.data)

def zeros(shape):
    """ Creates a matrix of the input shape with every element being a zero.

    Args:
        shape (tuple): A tuple containing the number of rows in the first index and the number of columns in the second index.
    Returns:
        Matrix: The matrix of zeros.
    """
    data = [0] * shape[0] * shape[1]
    mat = Matrix(data)
    return reshape(mat, shape)

def ones(shape):
    """ Creates a matrix of the input shape with every element being a one. 
    This function can then be used to create a matrix of any number using the scalar multiply function.

    Args:
        shape (tuple): A tuple containing the number of rows in the first index and the number of columns in the second index.
    Returns:
        Matrix: The matrix of ones.
    """
    data = [1] * shape[0] * shape[1]
    mat = Matrix(data)
    return reshape(mat, shape)

def reshape(mat, shape):
    """ Reshapes a matrix by flattening it and then iterating over the new list using nested for loops.

    Args:
        mat (Matrix): The input matrix.
        shape (tuple): A tuple containing the number of rows in the first index and the number of columns in the second index.
    Returns:
        Matrix: The reshaped matrix.
    """
    result = []
    list_1d = flatten(mat.data)
    for i in range(0, shape[0]):
        row = []
        for j in range(0, shape[1]):
            row.append(list_1d[(shape[1]*i) + j])
        result.append(row)
    return Matrix(result)

def transpose(mat):
    """ Uses the same method as the reshape() function and reshapes the matrix by flipping the rows and columns.

    Args:
        mat (Matrix): The input matrix.
    Returns:
        Matrix: The transposed matrix.
    """
    result = []
    list_1d = flatten(mat.data)
    shape = (mat.shape()[1], mat.shape()[0])
    for i in range(0, shape[0]):
        row = []
        for j in range(0, shape[1]):
            row.append(list_1d[(shape[0]*j) + i])
        result.append(row)
    return Matrix(result)

def flatten(data):
    """ Converts a list to one dimension by combining each row in sequence.

    Args:
        data (list): The input list.
    Returns:
        list: The one dimensional list.
    """
    result = []
    for x in data:
        if hasattr(x, "__iter__"):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

def add(mat1, mat2):
    """ Adds two matrices together using element-wise addition.

    Args:
        mat1 (Matrix): The first input matrix.
        mat2 (Matrix): The second input matrix.
    Returns:
        Matrix: The resulting matrix from the addition of mat1 and mat2.
    """
    if mat1.shape() == mat2.shape():
        mat1_1d = flatten(mat1.data)
        mat2_1d = flatten(mat2.data)
        result = [mat1_1d[i] + mat2_1d[i] for i in range(len(mat1_1d))]

        return reshape(Matrix(result), mat1.shape())
    else:
        raise ValueError('Both matrices must have the same dimensions!')

def subtract(mat1, mat2):
    """ Subtracts two matrices together using element-wise subtraction.

    Args:
        mat1 (Matrix): The first input matrix.
        mat2 (Matrix): The second input matrix.
    Returns:
        Matrix: The resulting matrix from the subtraction of mat2 from mat1.
    """
    if mat1.shape() == mat2.shape():
        mat1_1d = flatten(mat1.data)
        mat2_1d = flatten(mat2.data)
        result = [mat1_1d[i] - mat2_1d[i] for i in range(len(mat1_1d))]

        return reshape(Matrix(result), mat1.shape())
    else:
        raise ValueError('Both matrices must have the same dimensions!')

def multiply_elementwise(mat1, mat2):
    """ Multiplies two matrices together using element-wise multiplication.

    Args:
        mat1 (Matrix): The first input matrix.
        mat2 (Matrix): The second input matrix.
    Returns:
        Matrix: The resulting matrix from the multiplication of mat1 and mat2.
    """
    if mat1.shape() == mat2.shape():
        mat1_1d = flatten(mat1.data)
        mat2_1d = flatten(mat2.data)
        result = [mat1_1d[i] * mat2_1d[i] for i in range(len(mat1_1d))]

        return reshape(Matrix(result), mat1.shape())
    else:
        raise ValueError('Both matrices must have the same dimensions!')

def multiply_scalar(mat, value):
    """ Multiplies every element in the matrix by the given scalar value.

    Args:
        mat (Matrix): The input matrix.
        value (int or float): The number that mat will be multipled by.
    Returns:
        Matrix: The resulting matrix from the multiplication of mat and value.
    """
    mat_1d = flatten(mat.data)
    result = [x * value for x in mat_1d]
    return reshape(Matrix(result), mat.shape())

def vector_dot_product(vec1, vec2):
    """ Calculates the dot product of two input vectors (one dimensional matrices). This will be useful in the matrix multiplication function.

    Args:
        vec1 (Matrix): The first input vector.
        vec2 (Matrix): The second input vector. Should have the same dimensions as vec1.
    Returns:
        int or float: The resulting dot product of vec1 and vec2.
    """
    if vec1.shape() == vec2.shape():
        if vec1.shape()[0] == 1:
            return sum(multiply_elementwise(vec1, vec2).data[0])
        else:
            raise ValueError('The input vector must be one dimensional.')
    else:
        raise ValueError('Both vectors must have the same dimensions!')

def multiply(mat1, mat2):
    """ Multiplies the two input matrices.

    Args:
        mat1 (Matrix): The first input matrix.
        mat2 (Matrix): The second input matrix. The number of rows in mat2 should be equal to the number of columns in mat1.
    Returns:
        Matrix: The resulting matrix from the multiplication of mat1 and mat2.
    """
    if mat1.shape()[1] == mat2.shape()[0]:
        result_shape = (mat1.shape()[0], mat2.shape()[1])
        result = zeros(result_shape).data
        for i in range(result_shape[0]):
            for j in range(result_shape[1]):
                row = []
                if hasattr(mat1.data[i], "__iter__"):
                    row = Matrix(mat1.data[i])
                else:
                    row = mat1
                column = Matrix([row[j] for row in mat2.data])
                result[i][j] = vector_dot_product(row, column)
        return Matrix(result)
    else:
        raise ValueError('The number of columns in mat1 must equal the number of rows in mat2.')
