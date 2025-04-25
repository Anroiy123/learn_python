"""Nhập vào số dương, nếu nhập sai nhập lại cho đến khi đúng, nếu nhập đúng thì
xuất số đã nhập.
"""

try:
    n = -1
    while n <= 0:
        n = float(input('Nhập vào một số dương: '))
    print(n)

except ValueError:
    print('lỗi nhập số nguyên không hợp lệ!')