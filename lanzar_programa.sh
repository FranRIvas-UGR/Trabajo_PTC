#!/bin/bash

echo "Seleccione un módulo para lanzar:"
echo "1) Calcular promedio desde 1 hasta N"
echo "2) Calcular factorial de N"
echo "3) Calcular producto de dos matrices aleatorias de N x N"
echo "4) Sumar los numeros del 1 al N"
echo "5) Buscar el punto 2D vecino más cercano en un conjunto de N puntos 2D"
echo "6) Salir"
echo "-----º-----"
read -p "Introduzca el número del índice correspondiente: " indice
echo "-----º-----"

case $indice in
    1)
        read -p "Introduzca el valor de N: " n
        echo "Calculando promedio desde 1 hasta $n..."
        sleep 2
        echo "Se mostrará la diferencia de tiempo entre la ejecución en C++ y Python."
        cd Calcular_Promedio
        # Aquí puedes agregar el comando para lanzar el Módulo 1 con el valor de N
        ;;
    2)
        read -p "Introduzca el valor de N: " n
        if [ $n -gt 996 ]; then
            echo "El valor de N es mayor a 996. Por favor, introduzca un valor menor por temas de recursividad."
            exit 1
        fi
        echo "Calculando factorial de $n..."
        sleep 2
        echo "Se mostrará la diferencia de tiempo entre la ejecución en C++ y Python. (Los valores pequeños no ofrecen información relevante)"
        cd Factorial
        ;;
    3)
        read -p "Introduzca el valor de N: " n
        echo "Calculando producto de dos matrices aleatorias de $n x $n..."
        sleep 2
        echo "Se mostrará la diferencia de tiempo entre la ejecución en C++ y Python."
        cd Multiplicacion_Datos_N_Dim
        ;;
    4)
        read -p "Introduzca el valor de N: " n
        echo "Calculando suma de los números del 1 al $n..."
        sleep 2
        echo "Se mostrará la diferencia de tiempo entre la ejecución en C++ y Python."
        cd Suma_Numeros
        ;;
    5)
        read -p "Introduzca el valor de N: " n
        echo "Calculando el punto 2D vecino más cercano en un conjunto de $n puntos 2D..."
        sleep 2
        echo "Se mostrará la diferencia de tiempo entre la ejecución en C++ y Python."
        cd Vecino_Mas_Cercano
        ;;
    
    6)
        echo "Saliendo..."
        exit 0
        ;;

    *)
        echo "Opción no válida."
        exit 1
        ;;
esac

echo "---º---"
sleep 1

python3.10 measure.py $n

echo "---º---"

cd ..