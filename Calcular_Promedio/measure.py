import time
import random
import sys
import calcular_promedio_boost_module

def calcular_promedio_puro(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)

def convertir_lista_a_np_array(lista):
    import numpy as np
    return np.array(lista)

if __name__ == "__main__":
    # Generar una lista de 10^8 números aleatorios
    num_elementos = sys.argv[1] if len(sys.argv) > 1 else 10**8
    num_elementos = int(num_elementos)
    lista = [random.uniform(0, 100) for _ in range(num_elementos)]
    
    # Calcular promedio con Boost.Python
    lista_np_array = convertir_lista_a_np_array(lista)
    start = time.time()
    resultado_boost = calcular_promedio_boost_module.calcular_promedio(lista_np_array)
    end = time.time()
    print(f"Boost.Python: {end - start:.6f} segundos, resultado: {resultado_boost}")

    # Calcular promedio en Python puro
    start = time.time()
    resultado_python = calcular_promedio_puro(lista)
    end = time.time()
    print(f"Python puro: {end - start:.6f} segundos, resultado: {resultado_python}")

    
