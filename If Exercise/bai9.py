x = float(input('Nhập số thực x: '))
f = 0
if x > 0:
    f = x**2 + 3*x + 5
    print('f(x) có nghiệm là:',f)
else:
    f = (-x)**2 - 3*x - 5
    print('f(x) có nghiệm là:',f)


