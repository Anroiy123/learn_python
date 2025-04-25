while True:
    try:
        n = int(input('Nhập vào 1 số nguyên dương: '))
        if n <= 0:
            print('Lỗi ! yêu cầu nhập vào số nguyên dương')
            continue
        break
    except ValueError:
        print('Lỗi nhập liệu! Yêu cầu nhập vào số nguyên dương')
        continue

s = 0
i = 1

while i <= n:
    tu = 1
    mau = i * (i + 1)
    s += tu / mau
    i+=1

print(f'S(0) là {s}')