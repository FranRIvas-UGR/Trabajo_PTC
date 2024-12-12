#!/bin/bash

rm -f my_module.so

g++ -o my_module.so -shared -fPIC my_module.cpp -I/usr/include/python3.10 -lboost_python310 -lpython3.10

if [ $? -eq 0 ]; then
    echo "Compilación exitosa"
else
    echo "Error en la compilación"
fi