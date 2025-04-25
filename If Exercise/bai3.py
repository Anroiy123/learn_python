year = int(input("Nhập năm: "))
if (year % 400 == 0) | ((year % 100 != 0) & (year % 4 == 0)):
    print('Năm {0} là năm nhuận'.format(year))
else:
    print('Năm {0} không phải là năm nhuận'.format(year))


