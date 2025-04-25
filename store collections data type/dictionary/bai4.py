'''
Cho hai danh sách khác nhau có cùng n phần tử nhập vào từ bàn phím. Danh sách thứ nhất a = {a0, a1, ..., an-1}
và danh sách thứ hai b = {b0, b1, ..., bn-1}. Hãy tạo ra một dictionary là mydict mà key là các giá trị trong a, còn
value của mydict là giá trị trong b.
'''

def create_dict(a, b):
    return dict(zip(a, b))

n = int(input("Enter the number of elements in the lists: "))
a = list()
b = list()

for i in range(n):
    a.append(input(f"Enter element {i+1} of list a: "))
    b.append(input(f"Enter element {i+1} of list b: "))

print(f"List a: {a}")
print(f"List b: {b}")
print(f"Dictionary: {create_dict(a, b)}")

