from copy import deepcopy
import math

# All matricies and vectors are defined as 2d arrays 
# Example [[1,2],[3,4]]
# The column length is the found with len(matrix)
# the row length is found with len(matrix[0])


def isMatrix(matrix):
    if isinstance(matrix, list):
        for element in matrix:
            if not isinstance(element, list):
                return False
    else:
        return False
    return True

def isSquareMatrix(matrix):

    if isMatrix(matrix):
        n = len(matrix)
        m = len(matrix[0])
        return n == m   
    else:
        return False

def isVector(vector):
    if isinstance(vector, list):
        if isinstance(vector[0], list):
            if len(vector) == 1 or len(vector[0]) == 1:
                return True
    else:
        return False
    return False

def isRowVector(vector):
    if isVector(vector):
        if len(vector[0]) == 1:
            return True
    return False

def isColVector(vector):
    if isVector(vector):
        if len(vector) == 1:
            return True
    return False

def getMatrixDims(matrix):
    if isMatrix(matrix):
        return len(matrix[0]), len(matrix)

    return -1, -1

def transpose(matrix): 
    if isVector(matrix):
        if isRowVector(matrix):
            result_vector = [[0 for x in range(len(matrix))] for y in range(1)]
            for i in range(len(matrix)):
                result_vector[0][i] = matrix[i][0]
            
            return result_vector
        else:
            result_vector = [[0 for x in range(1)] for y in range(len(matrix[0]))]

            for i in range(len(matrix[0])):
                result_vector[i][0] = matrix[0][i]

            return result_vector
    elif isMatrix(matrix):
        new_m, new_n = getMatrixDims(matrix)
        print("TODO")
    return -1
         
def scalarAdd(matrix, scalar):
    matrix_copy = deepcopy(matrix)

    if isMatrix(matrix_copy):
        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy[i])):
                matrix_copy[i][j] += scalar

        return matrix_copy
    elif isVector(matrix_copy):
        for i in range(len(matrix_copy)):
            matrix_copy[i] += scalar
        return matrix_copy
    else:
        return -1
    
def scalarMultiply(matrix, scalar):
    matrix_copy = deepcopy(matrix)

    if isMatrix(matrix_copy):
        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy[i])):
                matrix_copy[i][j] *= scalar

        return matrix_copy
    elif isVector(matrix_copy):
        for i in range(len(matrix_copy)):
            matrix_copy[i] *= scalar
        return matrix_copy
    else:
        return -1

def matAdd(matrix1, matrix2):
    n1, m1 = getMatrixDims(matrix1)
    n2, m2 = getMatrixDims(matrix2)

    if n1 == n2 and m1 == m2:
        result_matrix = [[0 for i in range(n1)] for j in range(m1)]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

        return result_matrix
    else:
        print("Error adding matricies. The matricies must be of equal dimensions")
        return -1

def matMul(matrix1, matrix2):
    rowLength1, colLength1 = getMatrixDims(matrix1)
    rowLength2, colLength2 = getMatrixDims(matrix2)

    if colLength1 == rowLength2:
        result_matrix = [[0 for x in range(rowLength1)] for y in range(colLength2)]

        for row in range(rowLength1):
            for col in range(colLength2):

                element_result = 0
                for i in range(colLength1):
                    element_result += matrix1[i][col] * matrix2[row][i]

                result_matrix[row][col] = element_result
        
        return result_matrix
    else:
        print("Error multiplying matricies. The number of columns of the 1st matrix must equal the number of rows of the 2nd matrix.")
        return -1
    
def elementIndex(matrix):
    print("TODO")

def normalize(vector):
    result_vector = deepcopy(vector)
    flag = isRowVector(result_vector)
    if flag:
        result_vector = transpose(result_vector)

    if isVector(result_vector):
        col_sum_of_squares = 0
        for i in range(len(result_vector[0])):
            col_sum_of_squares += result_vector[0][i] * result_vector[0][i]
        
        magnitude = math.sqrt(col_sum_of_squares)

        for i in range(len(result_vector[0])):
            result_vector[0][i] = result_vector[0][i] / magnitude
    else:
        print("Error normalizing. Not a valid vector")
        return -1

    if flag:
        return transpose(result_vector)
    else:
        return result_vector

def getEuclidianNorm(vector):
    result_vector = deepcopy(vector)
    flag = isRowVector(result_vector)
    if flag:
        result_vector = transpose(result_vector)

    if isVector(result_vector):
        col_sum_of_squares = 0
        for i in range(len(result_vector[0])):
            col_sum_of_squares += result_vector[0][i] * result_vector[0][i]
        
        magnitude = math.sqrt(col_sum_of_squares)
        return magnitude
    else:
        print("Error normalizing. Not a valid vector")
        return -1

def dotProduct(vector):
    print("TODO")

def qrFactorization(matrix):
    print("TODO")

def inverse(matrix):
    print("TODO")

def submatrix(matrix):
    print("TODO")
matrix_A = [[2 for x in range(5)] for y in range(5)] #initialize matrix of zeros with size n x n
matrix_D = [[3 for x in range(5)] for y in range(5)]
matrix_B = [[2], [2]]
matrix_C = [1]

matrix_X = [[1],[2],[3]]
matrix_Y = [[4,5,6]]

print(normalize(matrix_Y))