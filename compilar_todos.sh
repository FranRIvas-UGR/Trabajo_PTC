#!/bin/bash

# Cambiar al directorio donde se encuentra el script
cd "$(dirname "$0")"

for dir in */; do
    if [ -f "$dir/compilar.sh" ]; then
        echo "----------------------------------------"
        echo "Compilando módulo de $dir"
        (cd "$dir" && ./compilar.sh)
        echo "----------------------------------------"
    fi
done

echo "Compilación de todos los módulos exitosa."