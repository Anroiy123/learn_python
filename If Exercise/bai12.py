try:
    a = int(input('Nhập vào số nguyên a: '))
    b = int(input('Nhập vào số nguyên b: '))

    if b == 0:
        print('Lỗi : b không thể bằng 0')
    elif a % b == 0:
        print(f'{a} là bội số của {b}')
    else:
        print(f'{a} không là bội số của {b}')

except:
    print('Hãy nhập số nguyên hợp lệ')