'''
Định nghĩa một hàm nextPrime nhằm tìm và trả về kết quả là số nguyên tố xuất hiện đầu tiên mà lớn hơn số n. Giá trị
số n sẽ được gán như là tham số ngõ vào duy nhất của hàm. Viết chương trình chính (main) để đọc một số nguyên từ
người dùng và hiển thị số nguyên tố đầu tiên và lớn hơn số người dùng vừa nhập.

'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nextPrime(n):
    next_prime = n+1
    while True:
        if is_prime(next_prime):
            return next_prime
        next_prime+=1


def main():
   while True:
        try:
            number = int(input("Nhập một số nguyên: "))
            if number < 0:
                print("Vui lòng nhập một số nguyên dương.")
                continue
            prime_number = nextPrime(number)
            print(f"Số nguyên tố đầu tiên lớn hơn {number} là: {prime_number}")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

main()

