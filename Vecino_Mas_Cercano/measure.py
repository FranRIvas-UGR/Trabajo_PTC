import time
import random
import numpy as np

import sys

from nearest_neighbor import nearest_neighbor_search
from nearest_neighbor_boost_np import nearest_neighbor_search_boost_np


if __name__ == "__main__":
    
    n = sys.argv[1] if len(sys.argv) > 1 else 1000
    n = int(n)

    points = [[random.uniform(0, n), random.uniform(0, n)] for _ in range(n)]
    target = [random.uniform(0, n), random.uniform(0, n)]
    
    points_np = np.array(points)
    target_np = np.array(target)
    
    start = time.time()
    nearest_neighbor_search_boost_np(points_np, target_np)
    end = time.time()
    end = time.time()
    
    print(f"Tiempo en Python con Boost: {end - start}")
    
    start = time.time()
    nearest_neighbor_search(points, target)
    end = time.time()
    
    print(f"Tiempo en Python puro: {end - start}")
    
    
    
