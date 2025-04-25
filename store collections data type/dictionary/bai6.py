'''
Nhập vào một nội dung chuỗi ký tự bao gồm ký tự số và ký tự chữ. Đếm số chữ cái và chữ số trong chuỗi đó.
Input : Python@123
Output : “số ký tự chữ: 6, số ký tự là số: 3”
'''

s = input("Nhập vào một chuỗi ký tự: ")
count_alpha = sum(c.isalpha() for c in s)
count_digit = sum(c.isdigit() for c in s)
print(f"số ký tự chữ: {count_alpha}, số ký tự là số: {count_digit}")
