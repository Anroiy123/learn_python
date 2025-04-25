n = 8
A = []

for i in range(n):
    A.append(float(input('Nhập vào số thứ {0}: '.format(i+1))))

positive = []
negative = []
zero = []

for i in A:
    if i < 0:
        negative.append(i),
    elif i == 0:
        zero.append(i)
    else:
        positive.append(i)

print('số lượng số dương là:', len(positive))
print('số lượng số âm là:', len(negative))
print('số lượng số bằng 0 là:', len(zero))