'''
Xây dựng lớp tam giác với dữ liệu thành phần là chiều dài ba cạnh, màu sắc; các hàm thành phần gồm hàm tính
chu vi, hàm tính diện tích tam giác, hàm hiển thị thông tin về tam giác, hàm hiển thị loại tam giác (vuông, cân,
vuông - cân, đều, thường) . sử dụng getter và setter cho các thuộc tính của lớp tam giác.
'''

import math

class TamGiac:
    def __init__(self, canh1, canh2, canh3, mau_sac="Không xác định"):
        """Hàm khởi tạo với các cạnh và màu sắc"""
        self._canh1 = 0  # Thuộc tính private với dấu gạch dưới
        self._canh2 = 0
        self._canh3 = 0
        self._mau_sac = mau_sac
        
        # Sử dụng setter để kiểm tra và gán giá trị
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3
        self._kiem_tra_tam_giac()  # Kiểm tra tam giác hợp lệ
    
    # Getter và Setter cho canh1
    @property
    def canh1(self):
        return self._canh1
    
    @canh1.setter
    def canh1(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Chiều dài cạnh phải lớn hơn 0!")
        self._canh1 = gia_tri
    
    # Getter và Setter cho canh2
    @property
    def canh2(self):
        return self._canh2
    
    @canh2.setter
    def canh2(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Chiều dài cạnh phải lớn hơn 0!")
        self._canh2 = gia_tri
    
    # Getter và Setter cho canh3
    @property
    def canh3(self):
        return self._canh3
    
    @canh3.setter
    def canh3(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Chiều dài cạnh phải lớn hơn 0!")
        self._canh3 = gia_tri
    
    # Getter và Setter cho mau_sac
    @property
    def mau_sac(self):
        return self._mau_sac
    
    @mau_sac.setter
    def mau_sac(self, gia_tri):
        self._mau_sac = gia_tri
    
    def _kiem_tra_tam_giac(self):
        """Kiểm tra tam giác có hợp lệ không"""
        if (self.canh1 + self.canh2 <= self.canh3 or 
            self.canh2 + self.canh3 <= self.canh1 or 
            self.canh1 + self.canh3 <= self.canh2):
            raise ValueError("Ba cạnh không tạo thành tam giác!")
    
    def tinh_chu_vi(self):
        """Hàm tính chu vi tam giác"""
        return self.canh1 + self.canh2 + self.canh3
    
    def tinh_dien_tich(self):
        """Hàm tính diện tích tam giác bằng công thức Heron"""
        p = self.tinh_chu_vi() / 2  # Nửa chu vi
        return math.sqrt(p * (p - self.canh1) * (p - self.canh2) * (p - self.canh3))
    
    def loai_tam_giac(self):
        """Hàm xác định loại tam giác"""
        a, b, c = self.canh1, self.canh2, self.canh3
        edges = sorted([a, b, c])  # Sắp xếp để kiểm tra vuông
        a, b, c = edges[0], edges[1], edges[2]
        
        is_vuong = abs((a**2 + b**2) - c**2) < 1e-10  # Kiểm tra vuông
        is_can = a == b or b == c or a == c  # Kiểm tra cân
        is_deu = a == b == c  # Kiểm tra đều
        
        if is_deu:
            return "Đều"
        elif is_vuong and is_can:
            return "Vuông cân"
        elif is_vuong:
            return "Vuông"
        elif is_can:
            return "Cân"
        else:
            return "Thường"
    
    def hien_thi_thong_tin(self):
        """Hàm hiển thị thông tin tam giác"""
        print(f"Tam giác có các cạnh: {self.canh1}, {self.canh2}, {self.canh3}")
        print(f"Màu sắc: {self.mau_sac}")
        print(f"Chu vi: {self.tinh_chu_vi():.2f}")
        print(f"Diện tích: {self.tinh_dien_tich():.2f}")
        print(f"Loại tam giác: {self.loai_tam_giac()}")

# Ví dụ sử dụng lớp TamGiac
if __name__ == "__main__":
    try:
        # Tạo tam giác với các cạnh 3, 4, 5 và màu đỏ
        tam_giac = TamGiac(3, 4, 5, "Đỏ")
        
        # Hiển thị thông tin
        tam_giac.hien_thi_thong_tin()
        
        # Thử thay đổi cạnh bằng setter
        print("\nThay đổi cạnh 1 thành 6:")
        tam_giac.canh1 = 6
        tam_giac.hien_thi_thong_tin()
        
        # Thử thay đổi màu sắc
        print("\nThay đổi màu sắc thành Xanh:")
        tam_giac.mau_sac = "Xanh"
        tam_giac.hien_thi_thong_tin()
        
        # Tạo tam giác đều
        print("\nTạo tam giác đều:")
        tam_giac_deu = TamGiac(5, 5, 5, "Vàng")
        tam_giac_deu.hien_thi_thong_tin()
        
    except ValueError as e:
        print(f"Lỗi: {e}")