'''
Viết chương trình nhập vào một số nguyên n, hãy in ra bảng cửu chương của n
'''

n = int(input("Nhập vào số nguyên n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
    