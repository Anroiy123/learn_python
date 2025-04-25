'''
  In ra tất cả ước số của một số nguyên N nhập bởi người dùng.
'''

while True:
    try:
        n = int(input('Nhập số nguyên N: '))
        break
    except ValueError:
            print('Lỗi nhập liệu ! Yêu cầu nhập số nguyên')
            continue
    
print(f'Tất cả ước số của {n} là: ',end='')
for i in range(1,n+1):
     if n % i == 0:
          print(i, end=" ")
     
