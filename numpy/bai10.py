import numpy as np

def transpose(mat: np.ndarray) -> np.ndarray:
    return np.transpose(mat)

mat = np.array([[1, 2], [3, 4], [5, 6]])
result = transpose(mat)
print(result)