'''
    Viết chương trình cho phép nhập một list có n phần tử số nguyên (n ≥ 0). In ra danh sách các số nguyên tố.
'''

def is_nguyen_to(num):
    if num < 2:
        return False
    for i in (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input('Nhập vào số lượng phần tử n: '))
A = []

for i in range(n):
    a = int(input(f'Nhập vào số nguyên thứ {i+1}: '))
    A.append(a)

B = []
for i in A:
    if is_nguyen_to(i):
        B.append(i)

if not B:
    print('Không có phần tử nào')
else:
    print(f'danh sách các số nguyên tố là : {B}')