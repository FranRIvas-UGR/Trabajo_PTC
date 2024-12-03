import my_module
import time

def sum_numbers_boost(n):
    return my_module.sum_numbers(n)

def sum_numbers_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    n = 500000000

    start_time = time.time()
    result_boost = sum_numbers_boost(n)
    end_time = time.time()
    print(f"Resultado de la suma (Boost): {result_boost}")
    print(f"Tiempo de ejecución (Boost): {end_time - start_time} segundos")

    start_time = time.time()
    result_loop = sum_numbers_loop(n)
    end_time = time.time()
    print(f"Resultado de la suma (Loop): {result_loop}")
    print(f"Tiempo de ejecución (Loop): {end_time - start_time} segundos")
