'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Hãy sắp xếp list phần tử âm tăng dần,
dương giảm dần.
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n):
    a = int(input(f'nhập vào phần tử thứ {i+1}: '))
    A.append(a)

B = []
C = []
 
for i in A:
    if i < 0:
        B.append(i)
    else:
        C.append(i)

B.sort()
C.sort(reverse=True)
D = B + C
print(D)