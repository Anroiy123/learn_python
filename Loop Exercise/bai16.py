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

s = 1
i = 2

while i <= n:
    tong = 0
    j = 1
    while j <= i:
        tong+=j
        j+=1
    s +=1/ tong
    i+=1


print(f'S(0) là {s}')