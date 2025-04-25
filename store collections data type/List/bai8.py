'''
Viết chương trình cho phép nhập một list có n phần tử bất kỳ (n ≥ 0). Hãy xuất ra danh sách chứa các phần tử
không trùng lặp (phần tử phân biệt chỉ xuất hiện duy nhất một lần)
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n):
    a = float(input(f'nhập vào phần tử thứ {i+1}: '))
    A.append(a)

B = []
for i in A:
    if A.count(i) == 1:
        B.append(i)

if not B:
    print('không có phần tử nào chỉ xuất hiện 1 lần')
else:
    print(f'danh sách các phần tử không trùng lặp là: {B}')