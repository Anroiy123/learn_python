'''
Xây dựng lớp toán học với dữ liệu thành phần gồm n số; các hàm thành phần gồm:
a. Hàm TinhTong(*nso): hàm tính tổng n số
b. Hàm TinhTrungBinh(*nso): hàm tính trung bình cộng của n số
c. Hàm TimMax(*nso): hàm tìm số lớn nhất của n số
d. Hàm TimMin(*nso): hàm tìm số nhỏ nhất của n số
e. Hàm HienThi(): hàm hiển thị thông tin về n số ra màn hình
có sử dụng phương thức getter và setter
'''

class ToanHoc:
    def __init__(self, *nso):
        """Hàm khởi tạo với n số"""
        self._danh_sach_so = []  # Thuộc tính private với dấu gạch dưới
        # Sử dụng setter để kiểm tra và gán giá trị
        self.danh_sach_so = list(nso) if nso else []
    
    # Getter cho danh_sach_so
    @property
    def danh_sach_so(self):
        return self._danh_sach_so
    
    # Setter cho danh_sach_so
    @danh_sach_so.setter
    def danh_sach_so(self, gia_tri):
        if not isinstance(gia_tri, (list, tuple)):
            raise ValueError("Danh sách số phải là list hoặc tuple!")
        if not gia_tri:
            raise ValueError("Danh sách số không được rỗng!")
        if not all(isinstance(x, (int, float)) for x in gia_tri):
            raise ValueError("Tất cả phần tử trong danh sách phải là số!")
        self._danh_sach_so = list(gia_tri)
    
    def tinh_tong(self, *nso):
        """Hàm tính tổng n số"""
        if nso:  # Nếu có tham số mới được truyền vào
            return sum(nso)
        return sum(self.danh_sach_so)  # Nếu không, dùng danh sách trong lớp
    
    def tinh_trung_binh(self, *nso):
        """Hàm tính trung bình cộng của n số"""
        if nso:
            return sum(nso) / len(nso)
        return sum(self.danh_sach_so) / len(self.danh_sach_so)
    
    def tim_max(self, *nso):
        """Hàm tìm số lớn nhất của n số"""
        if nso:
            return max(nso)
        return max(self.danh_sach_so)
    
    def tim_min(self, *nso):
        """Hàm tìm số nhỏ nhất của n số"""
        if nso:
            return min(nso)
        return min(self.danh_sach_so)
    
    def hien_thi(self):
        """Hàm hiển thị thông tin về n số"""
        print(f"Danh sách các số: {self.danh_sach_so}")
        print(f"Tổng: {self.tinh_tong():.2f}")
        print(f"Trung bình cộng: {self.tinh_trung_binh():.2f}")
        print(f"Số lớn nhất: {self.tim_max()}")
        print(f"Số nhỏ nhất: {self.tim_min()}")

# Ví dụ sử dụng lớp ToanHoc
if __name__ == "__main__":
    try:
        # Tạo đối tượng với 5 số
        toan = ToanHoc(1, 2, 3, 4, 5)
        
        # Hiển thị thông tin ban đầu
        print("Thông tin ban đầu:")
        toan.hien_thi()
        
        # Thử thay đổi danh sách số bằng setter
        print("\nThay đổi danh sách số thành [10, 20, 30]:")
        toan.danh_sach_so = [10, 20, 30]
        toan.hien_thi()
        
        # Thử gọi hàm với danh sách số mới
        print("\nThử tính tổng và trung bình với số mới:")
        print(f"Tổng mới: {toan.tinh_tong(5, 10, 15)}")
        print(f"Trung bình mới: {toan.tinh_trung_binh(5, 10, 15)}")
        
        # Thử gán danh sách không hợp lệ
        print("\nThử gán danh sách rỗng:")
        toan.danh_sach_so = []  # Sẽ ném ngoại lệ
        
    except ValueError as e:
        print(f"Lỗi: {e}")