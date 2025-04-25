'''
Viết chương trình cho phép nhập một list có n phần tử số nguyên (n ≥ 0). In ra danh sách các số chẵn/lẻ.
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []

for i in range(n):
    a = int(input(f'nhập vào phần tử thứ {i+1}: '))
    A.append(a)

B = []
C = []
for i in A:
    if i % 2 == 0:
        B.append(i)
    else :
        C.append(i)

print(f'danh sách các số chẵn là: {B}')
print(f'danh sách các số chẵn là: {C}')