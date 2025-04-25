a = int(input('Nhập số nguyen dương a: '))
b = int(input('Nhập số nguyên dương b: '))

a_chan = bool(a % 2 == 0)
b_chan = bool(b % 2 == 0)

if a_chan & b_chan:
    print('a va b la 2 so chan')
elif a_chan | b_chan:
    print('chi co mot so chan')
else:
    print('a va b là hai so le')