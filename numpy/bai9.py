import numpy as np

def broadcast(vec: np.ndarray, n: int) -> np.ndarray:
    return np.tile(vec.reshape(-1, 1), (1, n))

vec = np.array([6, 7])
n = 3
result = broadcast(vec, n)
print(result)