import numpy as np
array = np.random.randint(-10, 10, size=10)
positive_array = array[array > 0]
print(array)
print(positive_array)