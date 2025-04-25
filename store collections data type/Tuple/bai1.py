input_S =  input('Nhập vào 1 chuỗi các số phân tách bởi dấu (,): ')
Lst = [float(x) for x in input_S.split(",")]
tpl = tuple(Lst)
print(Lst)
print(tpl)