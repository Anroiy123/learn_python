'''
Khởi tạo list chứa giá trị nhiệt độ của 7 ngày trong tuần, giá trị nhiệt độ được nhập vào từ bàn phím. Tính nhiệt
độ trung bình của tuần. Đếm xem có bao nhiêu ngày nhiệt độ lớn hơn nhiệt độ trung bình của tuần đó.
'''

n = 7
A = []
average_temp = 0
for i in range(n):
    A.append(float(input(f'Nhập vào nhiệt độ ngày thứ {i+1}: ')))

for i in A:
    average_temp += i

average_temp /= 7

cnt = 0
for i in A:
    if i > average_temp :
        cnt+=1

if cnt == 0:
    print(f'Không có ngày nào có nhiệt độ lớn hơn nhiệt độ trung bình !')
else:
    print(f'số ngày có nhiệt độ lớn hơn nhiệt độ trung bình là: {cnt}')
