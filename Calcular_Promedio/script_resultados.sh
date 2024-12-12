#!/bin/bash

for i in 1000 10000 100000 1000000 10000000 100000000
do  
    echo "Calculando promedio con $i elementos"
    python3.11 measure.py $i
    echo "------------------------------"
done

