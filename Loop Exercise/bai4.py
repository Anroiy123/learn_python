'''
Nhập điểm lý thuyết, thực hành; kiểm tra riêng từng điểm phải trong khoảng từ [0 .. 10],
nếu không đúng phải nhập lại cho đến khi nào hợp lệ thì xuất điểm trung bình cộng. 
'''

try:
    a = float(input('Nhập điểm lý thuyết: '))
    while (a < 0) | (a > 10):
        a = float(input('Nhập lại điểm lý thuyết [0...10]: '))
    b = float(input('Nhập điểm thực hành: '))
    while (b < 0) | (b > 10):
        b = float(input('Nhập lại điểm thực hành [0...100]: '))
    print('trung bình cộng là :', (a+b)/2)

except ValueError:
    print('Nhập dữ liệu không đúng định dạng')