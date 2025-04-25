try:
    a = int(input('Nhập a: '))
    b = int(input('Nhập b: '))
    c = int(input('Nhập c: '))
    min = a
    if a < 0:
        min = b
    if b < 0:
        min = c

    if (b < min) & (b > 0):
        min = b
    elif (c < min) & (c > 0):
        min = c

    if (min <= 0):
        print('không có giá trị dương nào')
    else:
        print(f'giá trị nguyên dương nhỏ nhất là {min}')

except:
    print('Nhập số nguyên dương hợp lệ')
