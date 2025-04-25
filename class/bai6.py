'''
Viết chương trình quản lý học viên của một trung tâm AI sử dụng lớp gồm các chức năng sau đây:
a. Nhập thông tin các học viên đăng ký tại trung tâm và lưu vào tập tin dssv.txt, biết rằng: mỗi học viên khi
đến trung tâm đăng ký cần cung cấp các thông tin như sau:
✓Số CMND hoặc số Căn cước hoặc mã số giấy khai sinh
✓Họ tên học viên đăng ký
✓Năm sinh học viên
✓Danh sách các môn học mà học viên đăng ký tại trung tâm, mỗi môn gồm mã môn, tên môn và số tiết
b. Hiển thị thông tin của các học viên đã đăng ký tại trung tâm ra màn hình
c. Hiển thị thông tin của các học viên đăng ký ít nhất hai môn học tại trung tâm
d. Hiển thị thông tin môn học được nhiều sinh viên đăng ký nhất
e. Thống kê số lượng học viên trên mỗi môn học
'''

import json
from collections import Counter

# Lớp MonHoc để quản lý thông tin môn học
class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tiet):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tiet = so_tiet
    
    def __str__(self):
        return f"{self.ma_mon} - {self.ten_mon} ({self.so_tiet} tiết)"

# Lớp HocVien để quản lý thông tin học viên
class HocVien:
    def __init__(self, cmnd, ho_ten, nam_sinh, ds_mon_hoc=[]):
        self.cmnd = cmnd
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.ds_mon_hoc = ds_mon_hoc  # Danh sách các môn học
    
    def them_mon_hoc(self, mon_hoc):
        self.ds_mon_hoc.append(mon_hoc)
    
    def __str__(self):
        mon_hoc_str = "\n    ".join(str(mon) for mon in self.ds_mon_hoc)
        return f"CMND: {self.cmnd}\nHọ tên: {self.ho_ten}\nNăm sinh: {self.nam_sinh}\nDanh sách môn học:\n    {mon_hoc_str}"

# Lớp QuanLyHocVien để quản lý toàn bộ trung tâm
class QuanLyHocVien:
    def __init__(self):
        self.danh_sach_hv = []
        self.ten_tap_tin = "dssv.txt"
    
    def nhap_thong_tin(self):
        """Chức năng a: Nhập thông tin học viên và lưu vào tập tin"""
        print("Nhập thông tin học viên (nhấn Enter để kết thúc CMND):")
        while True:
            cmnd = input("Số CMND/Căn cước/Mã khai sinh: ").strip()
            if not cmnd:
                break
            ho_ten = input("Họ tên: ").strip()
            nam_sinh = int(input("Năm sinh: "))
            
            hv = HocVien(cmnd, ho_ten, nam_sinh)
            print("Nhập danh sách môn học (nhấn Enter để kết thúc mã môn):")
            while True:
                ma_mon = input("Mã môn: ").strip()
                if not ma_mon:
                    break
                ten_mon = input("Tên môn: ").strip()
                so_tiet = int(input("Số tiết: "))
                hv.them_mon_hoc(MonHoc(ma_mon, ten_mon, so_tiet))
            
            self.danh_sach_hv.append(hv)
        
        # Lưu vào tập tin
        self.luu_vao_tap_tin()
    
    def luu_vao_tap_tin(self):
        """Lưu danh sách học viên vào tập tin dssv.txt"""
        data = [
            {
                "cmnd": hv.cmnd,
                "ho_ten": hv.ho_ten,
                "nam_sinh": hv.nam_sinh,
                "ds_mon_hoc": [{"ma_mon": mon.ma_mon, "ten_mon": mon.ten_mon, "so_tiet": mon.so_tiet} for mon in hv.ds_mon_hoc]
            }
            for hv in self.danh_sach_hv
        ]
        with open(self.ten_tap_tin, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def doc_tu_tap_tin(self):
        """Đọc danh sách học viên từ tập tin dssv.txt"""
        try:
            with open(self.ten_tap_tin, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.danh_sach_hv = [
                    HocVien(
                        hv["cmnd"],
                        hv["ho_ten"],
                        hv["nam_sinh"],
                        [MonHoc(mon["ma_mon"], mon["ten_mon"], mon["so_tiet"]) for mon in hv["ds_mon_hoc"]]
                    )
                    for hv in data
                ]
        except FileNotFoundError:
            print("Tập tin dssv.txt chưa tồn tại!")
    
    def hien_thi_tat_ca(self):
        """Chức năng b: Hiển thị thông tin tất cả học viên"""
        if not self.danh_sach_hv:
            print("Chưa có học viên nào!")
            return
        print("\nDanh sách tất cả học viên:")
        for hv in self.danh_sach_hv:
            print(hv)
            print("-" * 50)
    
    def hien_thi_hv_hai_mon(self):
        """Chức năng c: Hiển thị học viên đăng ký ít nhất 2 môn"""
        print("\nHọc viên đăng ký ít nhất 2 môn học:")
        co_hv = False
        for hv in self.danh_sach_hv:
            if len(hv.ds_mon_hoc) >= 2:
                print(hv)
                print("-" * 50)
                co_hv = True
        if not co_hv:
            print("Không có học viên nào đăng ký ít nhất 2 môn!")
    
    def mon_hoc_nhieu_hv_nhat(self):
        """Chức năng d: Tìm môn học được nhiều học viên đăng ký nhất"""
        if not self.danh_sach_hv:
            print("Chưa có học viên nào!")
            return
        
        ds_mon = [mon.ma_mon for hv in self.danh_sach_hv for mon in hv.ds_mon_hoc]
        if not ds_mon:
            print("Chưa có môn học nào được đăng ký!")
            return
        
        mon_nhieu_nhat = Counter(ds_mon).most_common(1)[0]  # (ma_mon, so_luong)
        for hv in self.danh_sach_hv:
            for mon in hv.ds_mon_hoc:
                if mon.ma_mon == mon_nhieu_nhat[0]:
                    print(f"\nMôn học được nhiều học viên đăng ký nhất:")
                    print(f"{mon} - {mon_nhieu_nhat[1]} học viên")
                    break
            else:
                continue
            break
    
    def thong_ke_mon_hoc(self):
        """Chức năng e: Thống kê số lượng học viên trên mỗi môn học"""
        if not self.danh_sach_hv:
            print("Chưa có học viên nào!")
            return
        
        ds_mon = [mon.ma_mon for hv in self.danh_sach_hv for mon in hv.ds_mon_hoc]
        if not ds_mon:
            print("Chưa có môn học nào được đăng ký!")
            return
        
        thong_ke = Counter(ds_mon)
        print("\nThống kê số lượng học viên trên mỗi môn học:")
        for hv in self.danh_sach_hv:
            for mon in hv.ds_mon_hoc:
                if mon.ma_mon in thong_ke:
                    print(f"{mon} - {thong_ke[mon.ma_mon]} học viên")
                    del thong_ke[mon.ma_mon]  # Xóa để tránh trùng lặp

# Chương trình chính
def main():
    qlhv = QuanLyHocVien()
    
    while True:
        print("\n=== QUẢN LÝ HỌC VIÊN TRUNG TÂM AI ===")
        print("1. Nhập thông tin học viên")
        print("2. Hiển thị tất cả học viên")
        print("3. Hiển thị học viên đăng ký ít nhất 2 môn")
        print("4. Hiển thị môn học được nhiều học viên đăng ký nhất")
        print("5. Thống kê số lượng học viên trên mỗi môn học")
        print("6. Thoát")
        
        lua_chon = input("Chọn chức năng (1-6): ")
        
        if lua_chon == "1":
            qlhv.nhap_thong_tin()
        elif lua_chon == "2":
            qlhv.doc_tu_tap_tin()
            qlhv.hien_thi_tat_ca()
        elif lua_chon == "3":
            qlhv.doc_tu_tap_tin()
            qlhv.hien_thi_hv_hai_mon()
        elif lua_chon == "4":
            qlhv.doc_tu_tap_tin()
            qlhv.mon_hoc_nhieu_hv_nhat()
        elif lua_chon == "5":
            qlhv.doc_tu_tap_tin()
            qlhv.thong_ke_mon_hoc()
        elif lua_chon == "6":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()