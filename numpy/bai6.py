import numpy as np
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
array = a + (b - a) * np.random.rand(10)
print(array)