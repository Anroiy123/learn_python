'''
Viết chương trình cho phép người dùng có thể chuyển đổi giá trị giữa các hệ thống số như hệ 2, hệ 10 và hệ 16. Nếu
người dùng lựa chọn hệ thống số không phù hợp với các hệ mà chương trình hỗ trợ thì chương trình sẽ in ra một
dòng thông báo. Hãy định nghĩa một số hàm chức năng khác nhau để thực hiện chuyển đổi giá trị từ sang hệ thập
phân, và hệ thập phân sang nhị phân hoặc thập lục. Chương trình chính (main) sẽ đọc các hệ cơ bản và giá trị số
muốn chuyển đổi từ người sử dụng.
'''

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while n > 0:
        hexadecimal = hex_digits[n % 16] + hexadecimal
        n //= 16
    return hexadecimal


def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal


def hexadecimal_to_decimal(hex_str):
    decimal = 0
    hex_digits = "0123456789ABCDEF"
    for digit in hex_str:
        decimal = decimal * 16 + hex_digits.index(digit.upper())
    return decimal


def main():
    print("Chương trình chuyển đổi giữa các hệ thống số:")
    print("1. Hệ nhị phân (2)")
    print("2. Hệ thập phân (10)")
    print("3. Hệ thập lục (16)")

    from_system = input("Nhập hệ thống số nguồn (2, 10, 16): ")
    to_system = input("Nhập hệ thống số đích (2, 10, 16): ")
    value = input("Nhập giá trị cần chuyển đổi: ")

    if from_system == "10":
        decimal_value = int(value)
    elif from_system == "2":
        decimal_value = binary_to_decimal(value)
    elif from_system == "16":
        decimal_value = hexadecimal_to_decimal(value)
    else:
        print("Hệ thống số nguồn không hợp lệ.")
        return

    if to_system == "10":
        result = decimal_value
    elif to_system == "2":
        result = decimal_to_binary(decimal_value)
    elif to_system == "16":
        result = decimal_to_hexadecimal(decimal_value)
    else:
        print("Hệ thống số đích không hợp lệ.")
        return

    print(f"Kết quả chuyển đổi từ hệ {from_system} sang hệ {to_system}: {result}")


main()