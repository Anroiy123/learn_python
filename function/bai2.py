'''
Viết chương trình tính trung vị của 3 điểm. Hãy định nghĩa một hàm nhận 3 tham số ngõ vào và trả về kết quả là
trung vị của các điểm đã nhận. Viết chương trình chính (main) để đọc 3 giá trị này từ người dùng và hiển thị kết
quả lên màn hình.
'''

def trung_vi(a,b,c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


def main():
    a = float(input("Nhập giá trị thứ nhất: "))
    b = float(input("Nhập giá trị thứ hai: "))
    c = float(input("Nhập giá trị thứ ba: "))

    result = trung_vi(a, b, c)
    print(f"Trung vị của 3 số {a}, {b}, {c} là: {result}")

main()
