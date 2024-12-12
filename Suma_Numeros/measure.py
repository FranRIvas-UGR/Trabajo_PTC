import time
import sys

import my_module
import python_sum_boost as psb

if __name__ == "__main__":
    n = sys.argv[1] if len(sys.argv) > 1 else 10**8
    
    n = int(n)

    start_time = time.time()
    result_boost = psb.sum_numbers_boost(n)
    end_time = time.time()
    #print(f"Resultado de la suma (Boost): {result_boost}")
    print(f"Tiempo de ejecución (Boost): {end_time - start_time} segundos")

    start_time = time.time()
    result_loop = psb.sum_numbers_loop(n)
    end_time = time.time()
    
    #print(f"Resultado de la suma (Loop): {result_loop}")
    print(f"Tiempo de ejecución (Python puro): {end_time - start_time} segundos")