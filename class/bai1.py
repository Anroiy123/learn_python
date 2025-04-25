import math

'''
. Xây dựng lớp hình tròn với dữ liệu thành phần là bán kính của hình tròn và các hàm thành phần gồm: 
hàm tính chu vi, hàm tính diện tích, hàm hiển thị thông tin về hình tròn đó. sử dụng getter và setter cho các thuộc tính
của lớp hình tròn.
'''

class Hinhtron:
    def __init__(self, r = 1): 
        if r <= 0:
            raise ValueError('ban kinh phai lon hon 1')
        self._r = r
    
    @property 
    def ban_kinh(self):
        return self._r
    @ban_kinh.setter
    def ban_kinh(self, value):
        if value <= 0:
            raise ValueError('ban kinh phai lon hon 1')
        self._r = value

    def tinh_chu_vi(self):
        return 2 * math.pi * self._r
    def tinh_dien_tich(self):
        return math.pi * self._r ** 2
    
    def show_Info(self):
        print(f'Hinh tron co ban kinh la {self._r}')
        print(f'Hinh tron co chu vi la: {self.tinh_chu_vi():.2f}')
        print(f'Hinh trong co dien tich la: {round(self.tinh_dien_tich(),2)}')

try:
    # Tạo hình tròn với bán kính 5
    hinh_tron = Hinhtron()
    
    # Hiển thị thông tin
    print("Thông tin hình tròn ban đầu:")
    hinh_tron.show_Info()
    
    # Thử thay đổi bán kính bằng setter
    print("\nThay đổi bán kính thành 10:")
    hinh_tron.ban_kinh = 10
    hinh_tron.show_Info()
    
    # Thử gán giá trị không hợp lệ
    print("\nThử gán bán kính âm:")
    hinh_tron.ban_kinh = -3  # Sẽ ném ngoại lệ
    
except ValueError as e:
    print(f"Lỗi: {e}")
