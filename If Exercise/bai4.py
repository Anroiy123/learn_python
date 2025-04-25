import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b/(2*a)
        return "Phương trình có nghiệm kép x1 = x2 = {0}".format(x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return "Phương trình có hai nghiệm phân biệt x1 = {0}, x2 = {1}".format(x1, x2)
    

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
result = giai_phuong_trinh_bac_hai(a, b, c)
print(result)

