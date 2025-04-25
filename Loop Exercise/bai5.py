'''
Nhập vào 1 số dương, giả sử luôn nhập đúng, xuất các số từ 1 đến số đó
Ví dụ: Nhap 5, Xuat 1 2 3 4 5
'''

try:
    a = float(input('Nhập vào 1 số dương: '))
    while(a < 0):
        a = float(input('Nhập lại số dương: '))

    for i in range(int(a)):
        print(i+1, end=' ')

except  ValueError:
    print('Nhập sai kiểu dữ liệu!')