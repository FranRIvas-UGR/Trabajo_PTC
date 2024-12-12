#!/bin/bash

if [ ! -f measure.py ]; then
    echo "No se encontró el archivo measure.py"
    exit 1
fi

if [ -f resultados.txt ]; then
    rm resultados.txt
fi

for i in $(seq 50 50 500);
do  
    echo "Calculando promedio con matrices de $i x $i elementos" >> resultados.txt
    python3.11 measure.py $i >> resultados.txt
    echo "------------------------------" >> resultados.txt
done

