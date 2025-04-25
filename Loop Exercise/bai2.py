try:
    n = int(input('Nhập vào một số nguyên: '))
    can = int(n**0.5)
    
    if can * can == n:
        print(f'{n} là số chính phương')
    else :
        can_tren = (can+1)**2
        if (n - can*can) > (can_tren - n):
            print(f'{n} không là số chính phương , số chính phương gần nhất là {can_tren}')
        else:
            print(f'{n} không là số chính phương , số chính phương gần nhất là {can*can}')
        
except ValueError:
    print('số nguyên không hợp lệ ! ')