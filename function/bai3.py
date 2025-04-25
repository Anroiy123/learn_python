'''
Số nguyên tố là số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính số đó. Viết một hàm với chức năng là kiểm
tra xem tham số đầu vào của hàm đó có phải là số nguyên tố không. Hàm này sẽ tính toán và trả về True nếu đó
là số nguyên tố và ngược lại thì trả về False. Viết chương trình chính (main) để đọc một số nguyên từ người
dùng và hiển thị thông điệp chỉ ra số vừa nhập có phải là số nguyên tố không?

'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Nhập một số nguyên: "))
        if is_prime(number):
            print(f"{number} là số nguyên tố.")
        else:
            print(f"{number} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

main()