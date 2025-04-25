'''
Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp for tìm phần tử chia hết cho 5 lớn nhất.
'''

A = []

while True:
    try:
        n = input('Nhập phần tử (hoặc nhấn \'c\' để thoát): ')
        if n == 'c' or n == 'C':
            break
        n = float(n)
        A.append(n)
    except ValueError:
        print('Lỗi: vui lòng nhập số hợp lệ!')
        continue

if not A:
    print('danh sách rỗng!')
else:
    max = None
    for i in A:
        if i % 5 == 0:
            if max is None or i > max:
                max = i
    if max is None:
        print('không có phần tử nào trong danh sách chia hết cho 5')
    else:
        print(f"phần tử chia hết cho 5 lớn nhất là {max}")
        print(f'danh sách: {A}')
