'''
Viết code kiểm tra biểu thức sau đúng không (True or False)
Kiểm tra với x = 𝜋,𝜋/2,4𝜋/3 với sin^2 (x) + cos^2 (x) = 1
'''

import math
x = math.pi
print(math.sin(x)**2 + math.cos(x)**2 == 1)

x = math.pi/2
print(math.sin(x)**2 + math.cos(x)**2 == 1)

x = 4*math.pi/3

print(math.sin(x)**2 + math.cos(x)**2 == 1)



