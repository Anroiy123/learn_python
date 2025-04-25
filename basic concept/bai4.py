'''
Viết chương trình nhập vào số xe (gồm 5 chữ số) của bạn. Cho biết số xe của bạn được mấy nút? (nếu số nút vượt quá 10 sẽ đến lại từ 1)
input : 12193 -> output : 6
input : 58741 -> output : 5
'''

n = int(input("Nhập số xe của bạn: "))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
if sum > 10:
    sum %= 10
print(f"Số xe của bạn được {sum} nút.")

