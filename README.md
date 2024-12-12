# Proyecto de Módulos de Boost.Python

Este proyecto contiene varios módulos de Boost.Python que implementan diferentes algoritmos y funciones matemáticas. Cada carpeta contiene un módulo específico con su respectivo código fuente en C++, scripts de Python para medir el rendimiento y scripts de compilación.

## Estructura del Proyecto

```
├── Calcular_Promedio
│   ├── calcular_promedio_boost_module.so
│   ├── calcular_promedio.cpp
│   ├── compilar.sh
│   ├── measure.py
│   ├── resultados.txt
│   └── script_resultados.sh
├── Factorial
│   ├── compilar.sh
│   ├── measure.py
│   ├── my_module.cpp
│   ├── my_module.so
│   ├── python_factorial_boost.py
│   ├── resultados.txt
│   └── script_resultados.sh
├── Multiplicacion_Datos_N_Dim
│   ├── compilar.sh
│   ├── measure.py
│   ├── my_module.cpp
│   ├── my_module.so
│   ├── python_numpy_boost.py
│   ├── resultados.txt
│   └── script_resultados.sh
├── Suma_Numeros
│   ├── compilar.sh
│   ├── measure.py
│   ├── my_module.cpp
│   ├── my_module.so
│   ├── python_sum_boost.py
│   ├── resultados.txt
│   └── script_resultados.sh
├── Vecino_Mas_Cercano
│   ├── compilar.sh
│   ├── measure.py
│   ├── my_module.cpp
│   ├── my_module.so
│   ├── nearest_neighbor_boost_np.so
│   ├── nearest_neighbor_boost.so
│   ├── nearest_neighbor.py
│   ├── __pycache__
│   │   └── nearest_neighbor.cpython-311.pyc
│   ├── resultados.txt
│   └── script_resultados.sh
|
├── lanzar_programa.sh
├── compilar_todos.sh
└──README.md
```

### Calcular_Promedio

- `calcular_promedio_boost_module.so`: Módulo compilado de Boost.Python.
- `calcular_promedio.cpp`: Código fuente en C++ que implementa la función de cálculo de promedio.
- `compilar.sh`: Script para compilar el módulo.
- `measure.py`: Script de Python para medir el rendimiento del cálculo de promedio usando Boost.Python y Python puro.

### Factorial

- `my_module.so`: Módulo compilado de Boost.Python.
- `my_module.cpp`: Código fuente en C++ que implementa la función de cálculo del factorial.
- `python_factorial_boost.py`: Script de Python para medir el rendimiento del cálculo del factorial usando Boost.Python y Python puro.

### Multiplicacion_Datos_N_Dim

- `my_module.so`: Módulo compilado de Boost.Python.
- `my_module.cpp`: Código fuente en C++ que implementa la multiplicación de matrices usando Eigen.
- `python_numpy_boost.py`: Script de Python para medir el rendimiento de la multiplicación de matrices usando Boost.Python y Python puro.

### Suma_Numeros

- `my_module.so`: Módulo compilado de Boost.Python.
- `my_module.cpp`: Código fuente en C++ que implementa la suma de números.
- `python_sum_boost.py`: Script de Python para medir el rendimiento de la suma de números usando Boost.Python y Python puro.

### Vecino_Mas_Cercano

- `nearest_neighbor_boost_np.so`: Módulo compilado de Boost.Python para búsqueda de vecino más cercano usando NumPy.
- `compilar.sh`: Script para compilar el módulo.
- `measure.py`: Script de Python para medir el rendimiento de la búsqueda de vecino más cercano usando Boost.Python y Python puro.
- `my_module.cpp`: Código fuente en C++ que implementa la búsqueda de vecino más cercano usando NumPy.
- `nearest_neighbor.py`: Implementación en Python puro de la búsqueda de vecino más cercano.



## Compilación

Cada carpeta contiene un script `compilar.sh` que se puede ejecutar para compilar el módulo correspondiente. Por ejemplo, para compilar el módulo de `Calcular_Promedio`, navega a la carpeta y ejecuta:

## Ejecución
Cada carpeta contiene un script de Python para medir el rendimiento de las funciones implementadas. Por ejemplo, para medir el rendimiento del cálculo de promedio, navega a la carpeta Calcular_Promedio y ejecuta:

```bash
cd Calcular_Promedio
./compilar.sh
```

```bash
cd Calcular_Promedio
python3.10 measure.py
```

## Requisitos
- Python 3.10
- Boost.Python
- NumPy

## Resultados
Vamos a ir viendo los resultados de cada módulo por separado.

### Cálculo del Promedio de una Lista de Números

Se genera una lista de n números aleatorios y se calcula el promedio de estos números.

Probamos desde 1000 números hasta 10^8 números para hacer la media. Los resultados obtenidos fueron los siguientes:

----------------------------------------------------------------------------------------------
| Cantidad de Números | Tiempo Boost.Python (s) | Tiempo Python Puro (s) | Rapidez Boost (%) |
|---------------------|-------------------------|------------------------|-------------------|
| 1,000               | 0.000004                | 0.000008               | 50.00             |
| 10,000              | 0.000009                | 0.000040               | 22.50             |
| 100,000             | 0.000073                | 0.000462               | 15.80             |
| 1,000,000           | 0.000558                | 0.002951               | 18.91             |
| 10,000,000          | 0.005499                | 0.030203               | 18.20             |
| 100,000,000         | 0.075063                | 0.493640               | 15.21             |
----------------------------------------------------------------------------------------------

Como se puede observar, el uso de Boost.Python mejora significativamente el rendimiento en comparación con la implementación en Python puro, llegando a ser hasta un **50%** más rápido realizando el cálculo de la media.

### Cálculo del Factorial de un Número
Probamos desde 150 hasta 950 para calcular el factorial. Los resultados obtenidos fueron los siguientes:

---------------------------------------------------------------------------------
| Número | Tiempo Boost.Python (s) | Tiempo Python Puro (s) | Rapidez Boost (%) |
|--------|-------------------------|------------------------|-------------------|
| 150    | 1.4066696166992188e-05  | 2.6941299438476562e-05 | 47.79             |
| 200    | 1.5020370483398438e-05  | 2.9325485229492188e-05 | 48.76             |
| 250    | 1.4543533325195312e-05  | 3.3855438232421875e-05 | 57.05             |
| 300    | 2.2411346435546875e-05  | 4.9591064453125e-05    | 54.82             |
| 350    | 2.1457672119140625e-05  | 5.4836273193359375e-05 | 60.88             |
| 400    | 3.218650817871094e-05   | 6.389617919921875e-05  | 49.63             |
| 450    | 2.86102294921875e-05    | 5.269050598144531e-05  | 45.70             |
| 500    | 3.24249267578125e-05    | 6.031990051269531e-05  | 46.24             |
| 550    | 3.552436828613281e-05   | 7.104873657226562e-05  | 50.00             |
| 600    | 4.410743713378906e-05   | 7.462501525878906e-05  | 40.90             |
| 650    | 4.8160552978515625e-05  | 8.845329284667969e-05  | 45.55             |
| 700    | 5.6743621826171875e-05  | 9.250640869140625e-05  | 38.68             |
| 750    | 7.295608520507812e-05   | 0.00011968612670898438 | 39.04             |
| 800    | 8.821487426757812e-05   | 0.00012612342834472656 | 30.05             |
| 850    | 7.867813110351562e-05   | 0.00011777877807617188 | 33.20             |
| 900    | 0.0001964569091796875   | 0.00022125244140625    | 11.20             |
| 950    | 0.00010323524475097656  | 0.00014400482177734375 | 28.30             |
---------------------------------------------------------------------------------

Como se puede observar, el uso de Boost.Python mejora significativamente el rendimiento en comparación con la implementación en Python puro, llegando a ser hasta un **60%** más rápido realizando el cálculo del factorial.

### Multiplicación de Datos N-Dimensionales

Se generan matrices aleatorias de tamaño n x n y se multiplican la primera matriz por la segunda matriz.

Probamos con matrices de 50x50 hasta 500x500 para realizar la multiplicación de matrices. Los resultados obtenidos fueron los siguientes:

-----------------------------------------------------------------------------------------------
| Tamaño de la Matriz | Tiempo Boost.Python (s) | Tiempo Python Puro (s) | Rapidez Boost (%) |
|---------------------|-------------------------|------------------------|-------------------|
| 50 x 50             | 0.008069                | 0.042499               | 81.01             |
| 100 x 100           | 0.034788                | 0.225429               | 84.57             |
| 150 x 150           | 0.071447                | 0.750974               | 90.49             |
| 200 x 200           | 0.126700                | 1.773797               | 92.86             |
| 250 x 250           | 0.198439                | 3.563089               | 94.43             |
| 300 x 300           | 0.360034                | 6.884756               | 94.77             |
| 350 x 350           | 0.457721                | 10.050846              | 95.45             |
| 400 x 400           | 0.637957                | 15.889229              | 95.98             |
| 450 x 450           | 0.909405                | 22.435009              | 95.95             |
| 500 x 500           | 1.303077                | 31.573281              | 95.87             |
-----------------------------------------------------------------------------------------------

Como se puede observar, el uso de Boost.Python mejora significativamente el rendimiento en comparación con la implementación en Python puro, llegando a ser hasta un **95.98%** más rápido realizando la multiplicación de matrices, una verdadera mejora en comparación con la implementación en Python puro.

### Suma de Números

Se suman los números de 1 hasta n.

Probamos con 10000 números hasta 10^9 números para realizar la suma. Los resultados obtenidos fueron los siguientes:

----------------------------------------------------------------------------------------------
| Cantidad de Números | Tiempo Boost.Python (s) | Tiempo Python Puro (s) | Rapidez Boost (%) |
|---------------------|-------------------------|------------------------|-------------------|
| 10,000              | 0.000025                | 0.000200               | 87.50             |
| 100,000             | 0.000157                | 0.002088               | 92.48             |
| 1,000,000           | 0.002200                | 0.019140               | 88.51             |
| 10,000,000          | 0.016671                | 0.167597               | 90.05             |
| 100,000,000         | 0.152786                | 1.698332               | 91.00             |
| 500,000,000         | 0.763835                | 8.992313               | 91.51             |
| 1,000,000,000       | 1.554866                | 28.294063              | 94.50             |
----------------------------------------------------------------------------------------------

Como se puede observar, el uso de Boost.Python mejora significativamente el rendimiento en comparación con la implementación en Python puro, llegando a ser hasta un **94.50%** más rápido realizando la suma de números.

### Búsqueda del Vecino Más Cercano

Se generan n puntos aleatorios en un espacio de 2 dimensiones y se busca el vecino más cercano a un punto aleatorio.
Los puntos son una lista de n puntos en un espacio de 2 dimensiones y se elige un punto aleatorio. Se busca el punto más cercano a este punto aleatorio.

Este problema de búsqueda de vecino más cercano se realizó con 500.000 puntos hasta 5.000.000 puntos. Los resultados obtenidos fueron los siguientes:


-----------------------------------------------------------------------------------------------
| Cantidad de Puntos | Tiempo Boost.Python (s) | Tiempo Python Puro (s) | Rapidez Boost (%) |
|---------------------|-------------------------|------------------------|-------------------|
| 500,000             | 0.001984                | 0.071666               | 97.23             |
| 1,000,000           | 0.003923                | 0.142900               | 97.25             |
| 1,500,000           | 0.006831                | 0.218707               | 96.88             |
| 2,000,000           | 0.008257                | 0.282706               | 97.08             |
| 2,500,000           | 0.010649                | 0.379709               | 97.20             |
| 3,000,000           | 0.011782                | 0.433970               | 97.28             |
| 3,500,000           | 0.014282                | 0.494870               | 97.11             |
| 4,000,000           | 0.016246                | 0.582281               | 97.21             |
| 4,500,000           | 0.017495                | 0.651928               | 97.32             |
| 5,000,000           | 0.020211                | 0.712084               | 97.16             |
-----------------------------------------------------------------------------------------------

Como se puede observar, el uso de Boost.Python mejora significativamente el rendimiento en comparación con la implementación en Python puro, llegando a ser hasta un **97.32%** más rápido realizando la búsqueda del vecino más cercano.



Este `README.md` proporciona una descripción clara y detallada de la estructura del proyecto, los archivos contenidos en cada carpeta, y las instrucciones para compilar y ejecutar los módulos.
