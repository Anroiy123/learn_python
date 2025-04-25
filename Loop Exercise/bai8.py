'''
Nhập vào lần lượt các số để tính ra giá trị lớn nhất, nếu nhập vào số 0 thì kết thúc việc nhập số. Xuất ra giá trị lớn
nhất trong các số đã nhập.

'''

n = -1 
A = []

while n != 0:
    try:
        n = float(input('Nhập vào số: '))
    except ValueError:
        print('Nhập liệu sai!')
    if n == 0:
        print('n = 0, kết thúc nhập liệu')
        break
    A.append(n)

if len(A)==0:
    print('không có số nào để tìm giá trị lớn nhất!')
else:
    max = A[0]
    for i in A:
        if i > max:
            max = i
    print(f'số lớn nhất là {max}')