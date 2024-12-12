#!/bin/bash

if [ ! -f measure.py ]; then
    echo "No se encontró el archivo measure.py"
    exit 1
fi

if [ -f resultados.txt ]; then
    rm resultados.txt
fi

for i in 10000 100000 1000000 10000000 100000000 500000000 1000000000 5000000000 10000000000;
do  
    echo "Calculando sumas de $i elementos" >> resultados.txt
    python3.11 measure.py $i >> resultados.txt
    echo "------------------------------" >> resultados.txt
done

