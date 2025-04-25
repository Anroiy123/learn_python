'''
Nhập vào 2 số nguyên khác 0 là tử và mẫu của một phân số, xuất ra giá trị thập phân của phân số, ví dụ nhập tử
là 5, nhập mẫu là 8 thì xuất ra giá trị phân số dạng thập phân là 0.625, và cho nhập tiếp hai số khác để tính. Chương
trình ngừng khi một trong hai số nhập vào là số 0.
'''

while True:
    try:
        a = int(input('Nhập số tử: '))
        if a == 0: print('kết thúc chương trình'); break
        b = int(input('Nhập số mẫu: '))
        if b == 0: print('kết thúc chương trình'); break
        print('giá trị thập phân là:',a/b)
    except ValueError:
        print('lỗi nhập liệu! Yêu cầu nhập số nguyên')
        continue