#!/bin/bash

# Compilar el módulo
g++ -shared -fPIC -o nearest_neighbor_boost_np.so my_module.cpp -I/usr/include/python3.10 -lboost_python310 -lboost_numpy310

# Comprobar si la compilación ha tenido éxito
if [ $? -eq 0 ]; then
    echo "Compilación exitosa."
else
    echo "Error en la compilación." >&2
    exit 1
fi