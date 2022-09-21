import sys
import os
import random
import math
import argparse

def isValidZeroElement(matrix, i, j):
    if i == j:
        return False
    elif matrix[i][j] == 0:
        return False
    else:
        return True

def generateRandomMatrix(n, density):
    matrix_A = [[0 for x in range(n)] for y in range(n)] #initialize matrix of zeros with size n x n
    num_elements = n * n
    num_nonzero_elements = n * n
    density_normalized = density / 100.0 

    #generate matrix A with random values, and diagonal values set to the cube root of n
    for i in range(n):
        for j in range(n):
            if(i != j):
                matrix_A[i][j] = random.random()
            else:
                matrix_A[i][j] = math.pow(n,1/3)

    #create list of valid element to zero
    row_indicies = []
    col_indicies = []
    for i in range(n):
        for j in range(n):
            if(i != j):
                row_indicies.append(i)
                col_indicies.append(j)

    valid_potential_zero_elements = list(zip(row_indicies, col_indicies)) 

    #remove non diagonal elements until the inputted density is achieved 
    while num_nonzero_elements / num_elements > density_normalized:
        element_to_zero = random.choice(valid_potential_zero_elements)
        valid_potential_zero_elements.remove(element_to_zero)
        i = element_to_zero[0]
        j = element_to_zero[1]

        if isValidZeroElement(matrix_A, i, j):
            matrix_A[i][j] = 0
            num_nonzero_elements -= 1

    """
    for i in matrix_A:
        for j in i:
            print(j,end = " ")
        print()
    """

    return matrix_A

def validateDensityValue(n, density):
    num_elements = n * n
    density_normalized = density / 100.0 
    minimum_density_noramlized = n / num_elements
    minimun_density = minimum_density_noramlized * 100.0
    if density_normalized < minimum_density_noramlized:
        sys.exit(f"Density value of {density} is too low for matrix of size {n}x{n}, density must be >= {minimun_density}")

def printHelpAndExit():
    print("usage: python3 GMRES.py n m density")
    print("n      \t: An integer that efines matrix of size n x n")
    print("m      \t: An integer that controls the number of arnoldi steps")
    print("density\t: A float that determines what % of elements are non-zero")
    sys.exit()

def parseCommandlineArguments():
    numCommandlineArgs = len(sys.argv) - 1

    if(numCommandlineArgs == 1 and sys.argv[1].lower() == "help"):
        printHelpAndExit()    
    elif(numCommandlineArgs != 3):
        sys.exit(f"ERROR: Expected 3 arguments, recieved {numCommandlineArgs}")

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        density = float(sys.argv[3])
        return n, m, density
    except ValueError:
        sys.exit("Error parsing command line arguments")

def main():
    n, m, density = parseCommandlineArguments()
    validateDensityValue(n, density)
    A = generateRandomMatrix(n, density)
    print(A)

if __name__ == '__main__':
    main()