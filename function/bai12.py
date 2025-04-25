'''
Viết hàm tính cos(x) bằng Taylor series. Gợi ý: sử dụng vòng lặp while (xem nội dung tuần 3). Công thức khai
triển Taylor của cos(x) xem tại: https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

'''

import math
def cos_taylor(x, n_terms=10):
    cos_x = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        cos_x += term
    return cos_x



if __name__ == "__main__":
    x = float(input("Nhập giá trị x (radian): "))
    n_terms = int(input("Nhập số lượng số hạng trong chuỗi Taylor: "))
    result = cos_taylor(x, n_terms)
    print(f"Giá trị của cos({x}) bằng chuỗi Taylor với {n_terms} số hạng là: {result}")
    
