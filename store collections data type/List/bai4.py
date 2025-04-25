'''
Viết chương trình cho phép nhập một list có n phần tử số thực (n ≥ 0) và giá trị k nguyên dương. Tìm vị trị
phần tử âm thứ k trong danh sách
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

while True:
    try:
        k = int(input('Nhập vào giá trị k: '))
        if k <= 0:
            print('lỗi! yêu cầu nhập lại')
            continue
        break
    except ValueError:
        print('lỗi! yêu cầu nhập lại')
        continue

dem = 0  # Đếm số phần tử âm đã tìm thấy
vi_tri = -1  # Lưu vị trí của phần tử âm thứ k
    
for i in range(len(A)):
    if A[i] < 0:
        dem += 1
        if dem == k:
            vi_tri = i
            break
    
# In kết quả
if vi_tri == -1:
    if dem == 0:
        print(f"Không có phần tử âm nào trong danh sách.")
    else:
        print(f"Chỉ có {dem} phần tử âm, không đủ phần tử âm thứ {k}.")
else:
    print(f"Vị trí của phần tử âm thứ {k} là: {vi_tri} (chỉ số bắt đầu từ 0)")

