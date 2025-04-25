'''
Xây dựng ứng dụng quản lý danh sách các giao dịch:
✓ Giao dịch vàng: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), đơn giá, số lượng, loại vàng có 3 loại 18k, 24k,
9999. Thành tiền được tính như sau: thành tiền = số lượng * đơn giá.
✓ Giao dịch tiền tệ: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), tỷ giá (cũng là đơn giá), số lượng, loại tiền tệ có 3
loại:USD, EUR, AUD, loại giao dịch mua/bán. Thành tiền được tính như sau:
▪ Nếu loại giao dịch là “mua”thì: thành tiền = số lượng * tỷ giá
▪ Nếu loại giao dịch là “bán” thì: thành tiền = (số lượng * tỷ giá)* 1.05
✓ Tính lợi nhuận theo ngày.
Dựa vào mô tả trên, hãy:
a. Tạo lớp GiaoDich với các thuộc tính và phương thức chung (giao dịch vàng cũng là giao dịch).
b. Tạo lớp GiaoDichTienTe kế thừa từ lớp GiaoDich với các thuộc tính riêng và phương thức cần thiết.
c. Nhập xuất danh sách các giao dịch.
d. Tính tổng số lượng cho từng loại.
e. Tính tổng thành tiền cho từng loại.
'''

from abc import ABC, abstractmethod
from datetime import datetime

# Lớp trừu tượng GiaoDich
class GiaoDich(ABC):
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong):
        self.ma_gd = ma_gd
        self.ngay_gd = datetime.strptime(ngay_gd, "%d/%m/%Y")  # Chuỗi ngày dạng dd/mm/yyyy
        self.don_gia = don_gia
        self.so_luong = so_luong
    
    @abstractmethod
    def tinh_thanh_tien(self):
        """Phương thức trừu tượng để tính thành tiền"""
        pass
    
    def __str__(self):
        return f"Mã GD: {self.ma_gd}, Ngày GD: {self.ngay_gd.strftime('%d/%m/%Y')}, Đơn giá: {self.don_gia}, Số lượng: {self.so_luong}"

# Lớp GiaoDichVang kế thừa từ GiaoDich
class GiaoDichVang(GiaoDich):
    LOAI_VANG = ["18k", "24k", "9999"]
    
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_vang):
        super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
        if loai_vang not in self.LOAI_VANG:
            raise ValueError("Loại vàng không hợp lệ!")
        self.loai_vang = loai_vang
    
    def tinh_thanh_tien(self):
        return self.so_luong * self.don_gia
    
    def __str__(self):
        return f"{super().__str__()}, Loại vàng: {self.loai_vang}, Thành tiền: {self.tinh_thanh_tien():.2f}"

# Lớp GiaoDichTienTe kế thừa từ GiaoDich
class GiaoDichTienTe(GiaoDich):
    LOAI_TIEN = ["USD", "EUR", "AUD"]
    LOAI_GD = ["mua", "ban"]
    
    def __init__(self, ma_gd, ngay_gd, ty_gia, so_luong, loai_tien, loai_gd):
        super().__init__(ma_gd, ngay_gd, ty_gia, so_luong)
        if loai_tien not in self.LOAI_TIEN:
            raise ValueError("Loại tiền tệ không hợp lệ!")
        if loai_gd not in self.LOAI_GD:
            raise ValueError("Loại giao dịch không hợp lệ!")
        self.loai_tien = loai_tien
        self.loai_gd = loai_gd
    
    def tinh_thanh_tien(self):
        thanh_tien = self.so_luong * self.don_gia
        if self.loai_gd == "ban":
            thanh_tien *= 1.05
        return thanh_tien
    
    def __str__(self):
        return f"{super().__str__()}, Loại tiền: {self.loai_tien}, Loại GD: {self.loai_gd}, Thành tiền: {self.tinh_thanh_tien():.2f}"

# Lớp QuanLyGiaoDich để quản lý danh sách giao dịch
class QuanLyGiaoDich:
    def __init__(self):
        self.danh_sach_gd = []
    
    def them_giao_dich(self, gd):
        self.danh_sach_gd.append(gd)
    
    def nhap_danh_sach(self):
        """Chức năng c: Nhập danh sách giao dịch"""
        print("Nhập danh sách giao dịch (nhấn Enter để kết thúc mã GD):")
        while True:
            ma_gd = input("Mã giao dịch: ").strip()
            if not ma_gd:
                break
            ngay_gd = input("Ngày giao dịch (dd/mm/yyyy): ").strip()
            don_gia = float(input("Đơn giá/Tỷ giá: "))
            so_luong = float(input("Số lượng: "))
            loai = input("Loại giao dịch (1: Vàng, 2: Tiền tệ): ").strip()
            
            if loai == "1":
                loai_vang = input("Loại vàng (18k/24k/9999): ").strip()
                gd = GiaoDichVang(ma_gd, ngay_gd, don_gia, so_luong, loai_vang)
            elif loai == "2":
                loai_tien = input("Loại tiền tệ (USD/EUR/AUD): ").strip()
                loai_gd = input("Loại GD (mua/ban): ").strip()
                gd = GiaoDichTienTe(ma_gd, ngay_gd, don_gia, so_luong, loai_tien, loai_gd)
            else:
                print("Loại giao dịch không hợp lệ!")
                continue
            
            self.them_giao_dich(gd)
    
    def xuat_danh_sach(self):
        """Chức năng c: Xuất danh sách giao dịch"""
        if not self.danh_sach_gd:
            print("Chưa có giao dịch nào!")
            return
        print("\nDanh sách giao dịch:")
        for gd in self.danh_sach_gd:
            print(gd)
            print("-" * 50)
    
    def tong_so_luong_theo_loai(self):
        """Chức năng d: Tính tổng số lượng cho từng loại"""
        tong_vang = {"18k": 0, "24k": 0, "9999": 0}
        tong_tien = {"USD": 0, "EUR": 0, "AUD": 0}
        
        for gd in self.danh_sach_gd:
            if isinstance(gd, GiaoDichVang):
                tong_vang[gd.loai_vang] += gd.so_luong
            elif isinstance(gd, GiaoDichTienTe):
                tong_tien[gd.loai_tien] += gd.so_luong
        
        print("\nTổng số lượng theo loại vàng:")
        for loai, sl in tong_vang.items():
            print(f"{loai}: {sl}")
        print("\nTổng số lượng theo loại tiền tệ:")
        for loai, sl in tong_tien.items():
            print(f"{loai}: {sl}")
    
    def tong_thanh_tien_theo_loai(self):
        """Chức năng e: Tính tổng thành tiền cho từng loại"""
        tong_vang = {"18k": 0, "24k": 0, "9999": 0}
        tong_tien = {"USD": 0, "EUR": 0, "AUD": 0}
        
        for gd in self.danh_sach_gd:
            if isinstance(gd, GiaoDichVang):
                tong_vang[gd.loai_vang] += gd.tinh_thanh_tien()
            elif isinstance(gd, GiaoDichTienTe):
                tong_tien[gd.loai_tien] += gd.tinh_thanh_tien()
        
        print("\nTổng thành tiền theo loại vàng:")
        for loai, tt in tong_vang.items():
            print(f"{loai}: {tt:.2f}")
        print("\nTổng thành tiền theo loại tiền tệ:")
        for loai, tt in tong_tien.items():
            print(f"{loai}: {tt:.2f}")
    
    def tinh_loi_nhuan_theo_ngay(self):
        """Tính lợi nhuận theo ngày (chỉ áp dụng cho giao dịch tiền tệ)"""
        loi_nhuan = {}
        for gd in self.danh_sach_gd:
            if isinstance(gd, GiaoDichTienTe):
                ngay = gd.ngay_gd.strftime("%d/%m/%Y")
                thanh_tien = gd.tinh_thanh_tien()
                if gd.loai_gd == "ban":
                    loi_nhuan[ngay] = loi_nhuan.get(ngay, 0) + (thanh_tien - gd.so_luong * gd.don_gia)
                else:  # mua
                    loi_nhuan[ngay] = loi_nhuan.get(ngay, 0) - thanh_tien
        
        print("\nLợi nhuận theo ngày:")
        for ngay, ln in loi_nhuan.items():
            print(f"{ngay}: {ln:.2f}")

# Chương trình chính
def main():
    qlgd = QuanLyGiaoDich()
    
    while True:
        print("\n=== QUẢN LÝ GIAO DỊCH ===")
        print("1. Nhập danh sách giao dịch")
        print("2. Xuất danh sách giao dịch")
        print("3. Tổng số lượng theo loại")
        print("4. Tổng thành tiền theo loại")
        print("5. Tính lợi nhuận theo ngày")
        print("6. Thoát")
        
        lua_chon = input("Chọn chức năng (1-6): ")
        
        if lua_chon == "1":
            qlgd.nhap_danh_sach()
        elif lua_chon == "2":
            qlgd.xuat_danh_sach()
        elif lua_chon == "3":
            qlgd.tong_so_luong_theo_loai()
        elif lua_chon == "4":
            qlgd.tong_thanh_tien_theo_loai()
        elif lua_chon == "5":
            qlgd.tinh_loi_nhuan_theo_ngay()
        elif lua_chon == "6":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()