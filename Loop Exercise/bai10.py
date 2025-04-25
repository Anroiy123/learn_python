'''
Nhập vào một số nguyên dương, kiểm tra nếu nhập không đúng phải nhập lại cho đúng. Tính tổng các chữ số
trong số nguyên và xuất kết quả. (Ví dụ nhập 307 thì xuất tổng là 10)
'''

while True:
    try:
        a = n = int(input('Nhập vào 1 số nguyên dương: '))
        if n <= 0: print('Lỗi nhập liệu ! Nhập lại '); continue
        tong = 0
        while n != 0:
            tong = tong + (n%10)
            n = n // 10
        print(f'tổng các chữ số của {a} là:', tong)
        break
    except ValueError:
        print('Lỗi! Yêu cầu nhập vào số nguyên')
        continue