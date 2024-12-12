import time
import sys
import my_module
import python_numpy_boost as pnb
import numpy as np


def main():
    matrix_tam = sys.argv[1] if len(sys.argv) > 1 else 1000
    matrix_tam = int(matrix_tam)
    
    # Generate a random matrix of the given size
    matrixA = np.random.rand(matrix_tam, matrix_tam)
    matrixB = np.random.rand(matrix_tam, matrix_tam)
    
    start_time = time.time()
    my_module.matrix_multiply(matrixA, matrixB)
    end_time = time.time()
    print(f"Tiempo de ejecución (Boost): {end_time - start_time} segundos")
    
    
    start_time = time.time()
    pnb.matrix_multiply(matrixA, matrixB)
    end_time = time.time()
    print(f"Tiempo de ejecución (Python puro): {end_time - start_time} segundos")
    

if __name__ == "__main__":
    main()