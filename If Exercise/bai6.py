n = 5
a = []
for i in range(n):
    a.append(float(input('Nhập số thứ {0}: '.format(i+1))))

max = a[0]
min = a[0]
for i in a:
    if i > max :
        max = i
    if i < min :
        min = i 

print('max là : ', max)
print('min là : ', min)
