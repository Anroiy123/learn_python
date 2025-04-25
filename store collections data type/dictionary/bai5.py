'''
Thống kê điểm thi: Hãy viết chương trình nhập thông tin của học sinh, bao gồm: điểm, tên và lưu thông tin này
trong một từ điển gọi là mydict, với điểm nằm trong miền [0 .. 10], tên học sinh là một chuỗi ký tự nhập vào
Yêu cầu: Thống kê số lượng học sinh đạt được các mốc điểm 10, 8, ..., 0 và in ra kết quả.
'''

n = int(input("Enter the number of students: "))
mydict = dict()

for i in range(n):
    while True:
        try:
            name = input(f"Enter the name of student {i+1}: ")
            if not name:
                print("Lỗi: Tên không được để trống!")
                continue
            score = int(input(f"Enter the score of student {name} (0-10): "))
            if score < 0 or score > 10:
                print("Lỗi: Điểm phải nằm trong miền [0 .. 10]!")
                continue
            mydict[name] = score
            break
        except ValueError:
            print("Lỗi: Điểm phải là số nguyên hợp lệ (0-10)!")
        
print(f"Dictionary: {mydict}")
print("Thống kê điểm:")
for i in range(11):
    count = sum(value == i for value in mydict.values())
    print(f"{i}: {count} học sinh")
