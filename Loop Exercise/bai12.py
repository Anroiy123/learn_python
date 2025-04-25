'''
Nhập vào các số nguyên hoặc nhập 0 để kết thúc. Đếm số lượng các số âm có trong dãy số vừa nhập.
Ví dụ: nhập 3 8 -2 7 -5 1 0, dừng và xuất ra “Co 2 so am”
'''

cnt = 0
while True:
    try:
        n = int(input('Nhập vào số nguyên: '))
        if n == 0: print('Nhập liệu kết thúc!'); break
        if n < 0:
            cnt+=1
    except ValueError:
        print('Lỗi! Yêu cầu nhập vào số nguyên')
        continue
if cnt == 0: print('chưa có số âm nào được nhập')
else:
    print(f'Co {cnt} so am')