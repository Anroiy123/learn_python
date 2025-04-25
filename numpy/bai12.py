import numpy as np

def replace_col(mat: np.ndarray, col_ind: int) -> np.ndarray:
    mat[:, col_ind] = 1
    return mat

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
col_ind = 1
result = replace_col(mat, col_ind)
print(result)