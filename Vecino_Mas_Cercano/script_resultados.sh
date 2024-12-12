#!/bin/bash

if [ ! -f measure.py ]; then
    echo "No se encontró el archivo measure.py"
    exit 1
fi

if [ -f resultados.txt ]; then
    rm resultados.txt
fi

for i in $(seq 1 500000 5500000);
do  
    echo "Calculando vecinos más cercanos con $i elementos" >> resultados.txt
    python3.11 measure.py $i >> resultados.txt
    echo "------------------------------" >> resultados.txt
done

