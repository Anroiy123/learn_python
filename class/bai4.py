'''
Xây dựng lớp điểm để biểu diễn các điểm trong không gian hai chiều với dữ liệu thành phần gồm: tọa độ x
(hoành độ), tọa độ y (tung độ) và màu sắc của điểm; các hàm thành phần gồm:
a. Hàm khởi tạo dữ liệu điểm
b. Hàm hiển thị thông tin điểm
c. Hàm TinhTien(int x): tịnh tiến điểm đó theo trục hoành
d. Hàm TinhTien(int x, int y): tịnh tiến điểm đó theo cả hai hướng Ox, Oy
e. Hàm KhoangCach(): tính khoảng cách của điểm đó so với gốc tọa độ O(0, 0)
f. Hàm KhoangCach(Diem d): tính khoảng cách giữa hai điểm

'''

import math

class Diem:
    def __init__(self, x, y, color="Đen"):
        """Hàm khởi tạo dữ liệu điểm"""
        self._x = 0  # Thuộc tính private với dấu gạch dưới
        self._y = 0
        self._color = "Đen"
        # Sử dụng setter để gán giá trị ban đầu
        self.x = x
        self.y = y
        self.color = color
    
    # Getter và Setter cho x
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, gia_tri):
        if not isinstance(gia_tri, (int, float)):
            raise ValueError("Tọa độ x phải là số!")
        self._x = float(gia_tri)  # Chuyển thành float để nhất quán
    
    # Getter và Setter cho y
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, gia_tri):
        if not isinstance(gia_tri, (int, float)):
            raise ValueError("Tọa độ y phải là số!")
        self._y = float(gia_tri)
    
    # Getter và Setter cho color
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, gia_tri):
        if not isinstance(gia_tri, str):
            raise ValueError("Màu sắc phải là chuỗi!")
        self._color = gia_tri
    
    def hien_thi(self):
        """Hàm hiển thị thông tin điểm"""
        print(f"Điểm: ({self.x}, {self.y}) - Màu sắc: {self.color}")
    
    def tinh_tien(self, x, y=None):
        """Hàm tịnh tiến điểm"""
        if y is None:  # Chỉ tịnh tiến theo trục hoành
            self.x += x
        else:  # Tịnh tiến theo cả hai trục
            self.x += x
            self.y += y
    
    def khoang_cach(self, d=None):
        """Hàm tính khoảng cách"""
        if d is None:  # Tính khoảng cách đến gốc O(0, 0)
            return math.sqrt(self.x ** 2 + self.y ** 2)
        else:  # Tính khoảng cách đến điểm d
            if not isinstance(d, Diem):
                raise ValueError("Đối số phải là một đối tượng Diem!")
            return math.sqrt((self.x - d.x) ** 2 + (self.y - d.y) ** 2)

# Ví dụ sử dụng lớp Diem
if __name__ == "__main__":
    try:
        # Tạo một điểm
        d1 = Diem(3, 4, "Xanh")
        d1.hien_thi()  # Điểm: (3.0, 4.0) - Màu sắc: Xanh
        
        # Tịnh tiến theo trục hoành
        print("\nTịnh tiến theo Ox với x = 2:")
        d1.tinh_tien(2)
        d1.hien_thi()  # Điểm: (5.0, 4.0) - Màu sắc: Xanh
        
        # Tịnh tiến theo cả hai trục
        print("\nTịnh tiến theo Ox và Oy với x = 1, y = -3:")
        d1.tinh_tien(1, -3)
        d1.hien_thi()  # Điểm: (6.0, 1.0) - Màu sắc: Xanh
        
        # Tính khoảng cách đến gốc
        print(f"\nKhoảng cách đến gốc O: {d1.khoang_cach():.2f}")  # ~6.08
        
        # Tính khoảng cách đến một điểm khác
        d2 = Diem(0, 0, "Đỏ")
        print(f"Khoảng cách giữa d1 và d2: {d1.khoang_cach(d2):.2f}")  # ~6.08
        
        # Thử thay đổi thuộc tính bằng setter
        print("\nThay đổi tọa độ x thành 10:")
        d1.x = 10
        d1.hien_thi()  # Điểm: (10.0, 1.0) - Màu sắc: Xanh
        
        # Thử gán giá trị không hợp lệ
        d1.x = "abc"  # Sẽ ném lỗi
    except ValueError as e:
        print(f"Lỗi: {e}")