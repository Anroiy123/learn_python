'''
Viết chương trình tính giá trị biểu thức toán học sau và xuất kết quả: -b + sqrt(b^2 - 4ac) / 2a
'''

import math

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

if a == 0:
    print("Không thể chia cho 0")
elif (b ** 2) - (4 * a * c) < 0:
    print("Không thể tính căn bậc 2 của số âm")
else:
    print(f"Giá trị biểu thức toán học là: {(-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)}")
