n = 0
while n < 10000 or n > 99999:
    n = int(input('Nhập vào một số nguyên dương N với N ∈ [10000, 99999]: '))

A = []
chan = 0
le = 0

while n > 0:
    A.append(n % 10)
    n = n // 10

print(A)
for i in A:
    if i % 2 == 0:
        chan += 1
    else:
        le += 1

print(f'Số chữ số chẵn: {chan}')
print(f'Số chữ số lẻ: {le}')

