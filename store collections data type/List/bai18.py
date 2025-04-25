'''
Viết chương trình nhận giá trị là một số tự nhiên n. Trả về list số tự nhiên từ 0 → n và list bình phương các số tự
nhiên nhỏ hơn n.
'''

n = int(input('nhập vào 1 số tự nhiên n: '))
if n == 0:
    print('không có số nào nhỏ hơn 0')
else: 
    A = []
    B = []
    for i in range(n):
        A.append(i)
        B.append(i**2)

    print(A)
    print(B)

