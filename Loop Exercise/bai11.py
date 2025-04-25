'''
Nhập vào lần lượt các số và tính tổng các số dương, nếu nhập vào số 0 thì kết thúc việc nhập số. Xuất ra tổng các
số dương. Ví dụ: nhập 3 8 -2 7 -5 1 0, dừng và xuất ra 19
'''

n = -1
A = []
cnt = 0
while True:
    try:
        n = float(input('Nhập vào một số (0 để kết thúc): '))
        if n == 0: print('Kết thúc nhập liệu'); break
        if n > 0:
            cnt += n
    except ValueError:
        print('Lỗi, yêu cầu nhập số ')
        continue

print(f'tổng các số dương là: {cnt}')