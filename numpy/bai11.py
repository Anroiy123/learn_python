import numpy as np

def product(mat_a, mat_b):
    if mat_a.shape[1] == mat_b.shape[0]:
        matrix_product = np.matmul(mat_a, mat_b)
        print("Tich ma tran:")
        print(matrix_product)
    else:
        print("Khong co tich ma tran")

    if mat_a.shape == mat_b.shape:
        hadamard_product = np.multiply(mat_a, mat_b)
        print("Tich Hadamard:")
        print(hadamard_product)
    else:
        print("Khong co tich Hadamard")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
product(A, B)
