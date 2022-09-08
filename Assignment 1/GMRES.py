import sys
import os
import random
import math
import argparse

def parseCommandlineArguments():
    numCommandlineArgs = len(sys.argv) - 1

    if(numCommandlineArgs == 1 and sys.argv[1].lower() == "help"):
        print("usage: python3 GMRES.py n m density")
        print("n      \t: An integer that efines matrix of size n x n")
        print("m      \t: An integer that controls the number of arnoldi steps")
        print("density\t: A float that determines what % of elements are non-zero")
        sys.exit()
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
    print(f"{n} {m} {density}")

if __name__ == '__main__':
    main()