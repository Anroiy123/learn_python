'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0). Tìm vị trí phần tử âm đầu tiên.
'''

while True:
    try:
        n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
        if n < 0:
            print('lỗi! yêu cầu nhập lại')
            continue
        break
    except ValueError:
        print('lỗi! yêu cầu nhập lại')
        continue

A = []

for i in range(n):
    while True:
        try:
            a = float(input(f'Nhập vào phần tử thứ {i+1}: '))
            A.append(a)
            break
        except ValueError:
            print('lỗi! yêu cầu nhập lại') 
            continue

vi_tri = -1
for i in A:
    if i < 0:
        vi_tri = A.index(i)
        break

if vi_tri == -1:
    print('không có phần tử âm nào trong danh sách cả!')
else:
    print(f'vị trí của phần tử âm đầu tiên trong danh sách là: {vi_tri}')
