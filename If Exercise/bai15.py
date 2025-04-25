try:
    a = int(input('nhập a: '))
    b = int(input('nhập b: '))
    c = int(input('nhập c: '))

    A = [a,b,c]
    A.sort()
    print(f'số lớn nhì là {A[1]}')

except:
    print('Hãy nhập số nguyên hợp lệ')