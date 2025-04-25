'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Tính tổng các phần tử.
'''
A = []
while True:
    try:
        n = int(input('Nhập số lượng phần tử n(n>=0): '))
        if n < 0:
            print('lỗi! yêu cầu nhập lại')
            continue
        break
    except ValueError:
        print('lỗi! yêu cầu nhập lại')
        continue

if n == 0:
    print('không có phần tử nào')
else:
    for i in range(n):
        while True:
            try: 
                a = float(input(f'nhập vào phần tử thứ {i+1}: '))
                A.append(a)
                break
            except:
                print('Lỗi nhập liệu!')
    tong = 0
    for i in A:
        tong+=i
    print(f'tổng các phần tử là : {tong}')




