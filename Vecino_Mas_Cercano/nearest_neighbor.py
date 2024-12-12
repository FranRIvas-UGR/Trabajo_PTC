import numpy as np

def nearest_neighbor_search(data, point):
    data = np.array(data)
    point = np.array(point)
    distances = np.linalg.norm(data - point, axis=1)
    nearest_point_index = np.argmin(distances)
    return data[nearest_point_index].tolist()
