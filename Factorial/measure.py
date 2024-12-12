import my_module
import time
import sys

def factorial_boost(n):
    return my_module.factorial(n)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    n = sys.argv[1] if len(sys.argv) > 1 else 998
    n = int(n)
    start_time = time.time()
    result_boost = factorial_boost(n)
    end_time = time.time()
    #print(f"Factorial de {n} (Boost): {result_boost}")
    print(f"Tiempo de ejecución (Boost): {end_time - start_time} segundos")

    start_time = time.time()
    result = factorial(n)
    end_time = time.time()
    #print(f"Factorial de {n}: {result}")
    print(f"Tiempo de ejecución (Python puro): {end_time - start_time} segundos")