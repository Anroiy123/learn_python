'''
Viết chương trình nhập một số nguyên gồm 3 chữ số, giả sử luôn nhập đúng. Xuất trung bình cộng ba chữ số của
số nguyên đó: hàng trăm, hàng chục, hàng đơn vị.
'''

n = int(input("Nhập một số nguyên có 3 chữ số: "))
a = n // 100
b = (n % 100) // 10
c = n % 10
average = (a + b + c) / 3
print(f"Trung bình cộng ba chữ số của số nguyên {n} là: {average}")
