'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Hãy sắp xếp list phần tử âm giảm dần.
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n):
    a = float(input(f'nhập vào phần tử thứ {i+1}: '))
    A.append(a)

B = []

for i in A:
    if i < 0:
        B.append(i)
B.sort(reverse = True)
print(B)
