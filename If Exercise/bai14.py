try:
    a = int(input('Nhập số nguyên a:'))
    b = int(input('Nhập số nguyên b:'))
    c = int(input('Nhập số nguyên c:'))
    A = []
    
    if a % 2 == 0:
        A.append(a)
    if b % 2 == 0:
        A.append(b)
    if c % 2 == 0:
        A.append(c)
 
    if len(A) == 0:
        print('Khong co so chan nao')
    else: 
        max = A[0]
        for i in A:
            if i > max:
                max = i 
        print(f'số chẵn lớn nhất là {max}')
except:
    print('Nhập số nguyên hợp lệ')