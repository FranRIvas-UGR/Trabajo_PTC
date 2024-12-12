#!/bin/bash

# Eliminar archivos anteriores
rm -f calcular_promedio_boost_module.so

g++ -shared -fPIC -O3 -o calcular_promedio_boost_module.so calcular_promedio.cpp -I /usr/include/python3.10 -lboost_python310 -lpython3.10 -lboost_numpy310

# Comprobar si la compilación ha tenido éxito
if [ $? -eq 0 ]; then
    echo "Compilación exitosa."
else
    echo "Error en la compilación." >&2
    exit 1
fi