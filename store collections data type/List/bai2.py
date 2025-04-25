'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Tính trung bình cộng của n phần tử đó.
'''

n = int(input('nhập vào số lượng phần tử n(n>=0): '))
A = []

for i in range(n):
    a = float(input(f'Nhập vào phần tử thứ {i+1}: '))
    A.append(a)

tong = 0
for i in A: tong += i

print(f'trung bình cộng của {n} phần tử là: {tong/len(A)}')