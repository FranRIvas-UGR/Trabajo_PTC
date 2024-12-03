import my_module
import numpy as np
import time

def matrix_multiply_boost(A, B):
    return my_module.matrix_multiply(A, B)

def matrix_multiply(A, B):
    n = A.shape[0]
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]
    return result

if __name__ == "__main__":
    n = 500
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    start_time = time.time()
    result = matrix_multiply_boost(A, B)
    end_time = time.time()
    
    print(f"Tiempo de ejecución con Boost: {end_time - start_time} segundos")
    
    start_time_python = time.time()
    result_python = matrix_multiply(A, B)
    end_time_python = time.time()
    
    
    print(f"Tiempo de ejecución en Python: {end_time_python - start_time_python} segundos")
