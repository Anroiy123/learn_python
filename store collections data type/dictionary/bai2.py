'''
Cho phép người dùng nhập vào một dictionary, tìm tổng của tất cả value của dictionary này. Ví dụ:
dict = { 'a' : 100, 'b' : 200, 'c' : 300 } ➔ 600
'''

def sum_values(my_dict):  
    return sum(my_dict.values())

myDict = dict()

while True:
    try:
        n = int(input("Enter the number of elements in the dictionary: "))
        if n < 0:
            print("Lỗi: Số lượng phần tử phải lớn hơn hoặc bằng 0!")
            continue
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

for i in range(n):
    while True:
        try:
            key = input(f"Enter the key for element {i+1}: ")
            if not key:
                print("Lỗi: Key không được để trống!")
                continue
            value = float(input(f"Enter the value for key '{key}' (number): "))
            myDict[key] = value
            break
        except ValueError:
            print("Lỗi: Giá trị phải là số hợp lệ (ví dụ: 100, 200.5)!")

print(f"Dictionary vừa nhập: {myDict}")
print(f"Tổng của các giá trị trong dictionary là: {sum_values(myDict)}")