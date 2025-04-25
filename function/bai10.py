'''
Viết hàm nhận vào hai tham số: một list chứa tốc độ quay của một động cơ nào đó (list số nguyên), và một giá
trị min. Hàm trả về list các tốc độ quay nhỏ hơn min và indices của các tốc độ này.
'''

def speed_min(*args, min=0):
    return [x for x in args if x < min]

n = int(input('Nhập vào số lượng rotation speed: '))
A = []
for i in range(n):
    while True:
        try:
            m = int(input(f'nhập vào tốc độ vòng quay thứ {i+1}: '))
            if m < 0:
                print('lỗi! yêu cầu nhập vào tốc độ quay lớn hơn 0')
                continue
            A.append(m)
            break
        except ValueError:
            print('lỗi! yêu cầu nhập vào số nguyên')


m = int(input('Nhập vào giá trị min: '))
print('Tốc độ quay nhỏ hơn min là: ', speed_min(*A, min=m))
print('Các chỉ số của tốc độ quay nhỏ hơn min là: ', [i for i, x in enumerate(A) if x < m])




