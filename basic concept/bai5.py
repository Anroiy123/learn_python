'''
Viết chương trình nhập 2 số nguyên lưu vào 2 biến. Hoán vị (hoán đổi giá trị) 2 biến này.
'''

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
a, b = b, a

print(f"Sau khi hoán vị, a = {a}, b = {b}")
