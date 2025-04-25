'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Hãy sắp xếp list phần tử lẻ giảm dần,
chẵn tăng dần.
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n):
    a = int(input(f'nhập vào phần tử thứ {i+1}: '))
    A.append(a)

even = []
odd = []
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort(reverse=True)
A = odd + even
print(A)

