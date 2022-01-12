import numpy as np


def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return None
    else:
        return vector / norm


def normalized_connection_vector(start, end):
    normalized = normalize(end - start)
    return normalized


def phi(vector):
    if vector[1] == 0:
        if vector[0] < 0:
            return - np.pi / 2
        else:
            return np.pi / 2
    else:
        return np.arctan(vector[0] / - vector[1])
