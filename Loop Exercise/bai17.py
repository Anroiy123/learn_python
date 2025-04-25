'''
Cho người dùng nhập số nguyên dương N. Nếu nhập sai thì cho nhập lại đến khi đúng. Sau đó cho người dùng
nhập N số nguyên và in ra số lẻ lớn nhất trong những số được nhập. Cuối cùng, hỏi người dùng có muốn tiếp tục
không, nếu người dùng nhấn 'c' thì tiếp tục, nhấn phím khác thì thoát chương trình.
'''
A = []
B = []
while True:
    try:
        n = int(input('Nhập số nguyên dương N: '))
        if n<=0:
            print('Lỗi nhập liệu ! Yêu cầu nhập số nguyên dương')
            continue
        break
    except ValueError:
            print('Lỗi nhập liệu ! Yêu cầu nhập số nguyên dương')
            continue

while True:
     for i in range(n):
          A.append(int(input('Nhập vào số nguyên thứ {0}: '.format(i+1))))
     for i in A:
          if i % 2 != 0:
               B.append(i)
     print(max(B))
     x = str(input('Bạn có muốn tiếp tục không ? (press C to continue)...'))
     if ( x == "c" ) | (x == 'C'):
          continue
     else:
          break