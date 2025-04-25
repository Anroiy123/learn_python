'''
. Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp for xóa các phần tử lớn hơn A trong list, với A
là một số thực nhập bởi người dùng.

'''

A = []
while True:
    try:  
        n = float(input('Nhập vào phần tử: '))
    except ValueError:
        print('lỖI NHẬP LIỆU!')
        continue