'''
Viết chương trình cho phép nhập một list có n phần tử bất kỳ (n ≥ 0) và giá trị k, tìm xem trong list có tồn tại k
hay không? Nếu có hãy xóa tất cả các phần tử mang giá trị k và xuất danh sách
'''

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n):
    a = int(input(f'Nhập vào giá trị thứ {i+1}: '))
    A.append(a)

k = int(input('nhập vào giá trị k: '))
print('danh sách trước khi xoá là:', A)
for i in A:
    if i == k:
        A.remove(i)
print('danh sách sau khi xoá là:', A)
