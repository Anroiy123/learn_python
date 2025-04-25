'''
Với số nguyên n, hãy viết chương trình để tạo ra một dictionary chứa (i, i^2) như là số nguyên từ 1 → n (bao gồm
cả 1 và n) sau đó in ra dictionary này.
'''

def create_dict(n):
    return {i: i**2 for i in range(1, n+1)}

n = int(input("Enter an integer n: "))
print(create_dict(n))

