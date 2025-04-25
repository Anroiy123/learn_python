'''
 Nhập vào một số nguyên dương. Đếm xem có bao nhiêu ký tự số 7 trong số vừa nhập.
Ví dụ: nhập 37577 0, xuất ra “Co 3 so 7”
'''

cnt = 0

while True:
    try:
        a = n = int(input('nhập vào số nguyên dương: '))
        if n <= 0:
            print('Lỗi ! số cần nhập phải là số nguyên dương và lớn hơn 0')
            continue
        break
    except ValueError:
        print('Lỗi nhập liệu ! Yêu cầu nhập vào số nguyên dương')
        continue


while n != 0:
    if n % 10 == 7:
        cnt+=1
    n //= 10

if cnt == 0:
    print(f'{a} khong co so 7 nao')
else:
    print(f'Co {cnt} so 7')    

