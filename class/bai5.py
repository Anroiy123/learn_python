'''
Tính chu vi & diện tích các hình (abstract). Viết chương trình tính chu vi và điện tích của một số hình như sau:
a. Hình tròn
b. Hình chữ nhật
c. Hình tam giác
'''

from abc import ABC, abstractmethod
import math

# Lớp trừu tượng HinhHoc
class HinhHoc(ABC):
    @abstractmethod
    def tinh_chu_vi(self):
        """Phương thức trừu tượng để tính chu vi"""
        pass
    
    @abstractmethod
    def tinh_dien_tich(self):
        """Phương thức trừu tượng để tính diện tích"""
        pass

# Lớp HinhTron kế thừa từ HinhHoc
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        if ban_kinh <= 0:
            raise ValueError("Bán kính phải lớn hơn 0!")
        self.ban_kinh = ban_kinh
    
    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh
    
    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2
    
    def __str__(self):
        return f"Hình tròn (bán kính = {self.ban_kinh})"

# Lớp HinhChuNhat kế thừa từ HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        if chieu_dai <= 0 or chieu_rong <= 0:
            raise ValueError("Chiều dài và chiều rộng phải lớn hơn 0!")
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def __str__(self):
        return f"Hình chữ nhật (dài = {self.chieu_dai}, rộng = {self.chieu_rong})"

# Lớp HinhTamGiac kế thừa từ HinhHoc
class HinhTamGiac(HinhHoc):
    def __init__(self, canh1, canh2, canh3):
        if canh1 <= 0 or canh2 <= 0 or canh3 <= 0:
            raise ValueError("Các cạnh phải lớn hơn 0!")
        if canh1 + canh2 <= canh3 or canh2 + canh3 <= canh1 or canh1 + canh3 <= canh2:
            raise ValueError("Ba cạnh không tạo thành tam giác!")
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3
    
    def tinh_chu_vi(self):
        return self.canh1 + self.canh2 + self.canh3
    
    def tinh_dien_tich(self):
        # Công thức Heron
        p = self.tinh_chu_vi() / 2  # Nửa chu vi
        return math.sqrt(p * (p - self.canh1) * (p - self.canh2) * (p - self.canh3))
    
    def __str__(self):
        return f"Hình tam giác (các cạnh = {self.canh1}, {self.canh2}, {self.canh3})"

# Chương trình chính để tính chu vi và diện tích
def main():
    # Tạo danh sách các hình
    danh_sach_hinh = [
        HinhTron(5),              # Hình tròn bán kính 5
        HinhChuNhat(4, 6),        # Hình chữ nhật 4x6
        HinhTamGiac(3, 4, 5)      # Hình tam giác 3-4-5
    ]
    
    # Tính và hiển thị chu vi, diện tích cho từng hình
    for hinh in danh_sach_hinh:
        print(f"\n{hinh}")
        print(f"Chu vi: {hinh.tinh_chu_vi():.2f}")
        print(f"Diện tích: {hinh.tinh_dien_tich():.2f}")

if __name__ == "__main__":
    main()