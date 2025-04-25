'''
Khởi tạo list chứa n giá trị (n≥0). Không dùng hàm max/min, hãy tìm và in ra màn hình giá trị lớn nhất/nhỏ nhất
trong list.
'''

n = int(input('Nhập vào số phần tử n(n>=0): '))
A = []
for i in range(n):
    A.append(float(input(f'Nhập vào số thứ {i+1}: ')))

if not A:
    print('không có phần tử nào!')
else: 
    max = A[0]
    min = A[0]

    for i in A:
        if i > max:
            max = i
        if i < min:
            min = i

    print(f'giá trị lớn nhất là: {max}')
    print(f'giá trị nhỏ nhất là: {min}')
