'''
: Trong một ứng dụng có quản lý bất động sản của công ty ABC có 4 loại đối
tượng là: đất trồng, nhà ở, biệt thự và khách sạn. Biết rằng tất cả đối tượng này đều có
các thông tin sau: mã số, chiều dài, chiều rộng và phương thức khởi tạo, in thông tin,
tính giá trị. Biết rằng giá trị được tính như sau:
- Đất trồng: giá trị = diện tích * 30,000,000;
- Nhà ở có thêm thông tin về số lầu: giá trị = diện tích * 60,000,000 + số lầu *
100,000,000.
- Khách sạn có thêm thông tin về số sao: giá trị = diện tích * 70,000,000 + số sao * 50,000,000
- Biệt thự: giá trị = diện tích * 100,000,000
Trong 4 loại bất động sản trên thì có 2 loại là biệt thự và khách sạn phải đóng phí kinh
doanh. Phí kinh doanh được tính như sau:
- Biệt thự: chiều rộng * 5000
- Khách sạn: chiều rộng * 10000
Yêu cầu:
1. Thiết kế các lớp BatDongSan (lớp cha) và các lớp con: DatTrong, NhaO, KhachSan,
BietThu với các thuộc tính và chức năng như mô tả. Thiết kế giao diện PhiKinhDoanh
chứa một chức năng tính phí kinh doanh. Sau đó 2 lớp BietThu và KhachSan sẽ triển
khai giao diện PhiKinhDoanh.
2.Tại chương trình chính xây dựng các chức năng sau:
a) Nhập 1 danh sách bất động sản
b) Cho biết số lượng bất động sản theo từng loại
c) In ra danh sách các bất động sản có diện tích trên 1000
d) Tính tổng phí dinh doanh thu được
'''
import os 
from abc import ABC, abstractmethod


class PhiKinhDoanh(ABC):
    @abstractmethod
    def tinhPhiKinhDoanh(self):
        pass

class BatDongSan:
    def __init__(self, maSo, chieuDai, chieuRong):
        self.maSo = maSo
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
    def tinhDienTich(self):
        return self.chieuDai * self.chieuRong
    
    @abstractmethod
    def tinhGiaTri(self):
        pass
    def inThongTin(self):
        print(f'**Mã Số: {self.maSo},\n Chiều dài: {self.chieuDai},\n Chiều rộng: {self.chieuRong}')

class DatTrong(BatDongSan):
    def tinhGiaTri(self):
        return self.tinhDienTich() * 30000000
    def inThongTin(self):
        super().inThongTin()
        print(f'**Loại: Đất trồng, Giá trị: {self.tinhGiaTri()}')

class NhaO(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong, soLau):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soLau = soLau
    def tinhGiaTri(self):
        return self.tinhDienTich() * 60000000 + self.soLau * 100000000
    def inThongTin(self):
        super().inThongTin()
        print(f'**Loại: Nhà ở, số lầu: {self.soLau}, Giá trị: {self.tinhGiaTri()}')

class KhachSan(BatDongSan, PhiKinhDoanh):
    def __init__(self, maSo, chieuDai, chieuRong, soSao):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soSao = soSao
    def tinhGiaTri(self):
        return self.tinhDienTich() * 70000000 + self.soSao * 50000000
    def tinhPhiKinhDoanh(self):
        return self.chieuRong * 10000
    def inThongTin(self):
        super().inThongTin()
        print(f'**Loại: Khách sạn, Số sao: {self.soSao}, phí kinh doanh: {self.tinhPhiKinhDoanh()}, giá trị: {self.tinhGiaTri()}')

class BietThu(BatDongSan, PhiKinhDoanh):
    def tinhPhiKinhDoanh(self):
        return self.chieuRong * 5000
    def tinhGiaTri(self):
        return self.tinhDienTich() * 100000000
    def inThongTin(self):
        super().inThongTin()
        print(f'**Loại: Biệt thự, Phí kinh doanh: {self.tinhPhiKinhDoanh()}, giá trị: {self.tinhGiaTri()}')
    
def themBatDongSan(ds):
    while True:
        loai = int(input('Nhập loại: 1.Đất Trồng 2.Nhà Ở 3.Khách sạn 4.Biệt thự : '))
        if not loai:
            break
        maSo = input('Nhập mã số: ').strip()
        chieuDai = float(input('nhập chiều dài: '))
        chieuRong = float(input('Nhập chiều rộng: '))

        if loai == 1:
            bds = DatTrong(maSo, chieuDai, chieuRong)
        elif loai == 2:
            soLau = int(input('nhập số lầu: '))
            bds = NhaO(maSo, chieuDai, chieuRong, soLau)
        elif loai == 3:
            soSao = int(input('Nhập số sao: '))
            bds = KhachSan(maSo, chieuDai, chieuRong, soSao)
        elif loai == 4:
            bds = BietThu(maSo, chieuDai, chieuRong)
        else:
            print('loại bất động sản không hợp lệ: ')
            continue
    ds.append(bds)

def demSoLuongTheoLoai(ds):
    soLuongDatTrong = sum(isinstance(bds, DatTrong) for bds in ds)
    soLuongNhaO = sum(isinstance(bds, NhaO) for bds in ds)
    soLuongKhachSan = sum(isinstance(bds, KhachSan) for bds in ds)
    soLuongBietThu = sum(isinstance(bds, BietThu) for bds in ds)
    print(f'số lượng đất trồng là: {soLuongDatTrong}')
    print(f'số lượng nhà ở là: {soLuongNhaO}')
    print(f'số lượng khách sạn là: {soLuongKhachSan}')
    print(f'số lượng biệt thự là: {soLuongBietThu}')

def inDanhSachDienTichLon(ds):
    print(f'danh sách bđs có diện tích trên 1000: ')
    for bds in ds:
        if bds.tinhDienTich() > 1000:
            bds.inThongTin()
            print('-'*10)

def tinhTongPhiKinhDoanh(ds):
    tongPhi = sum(bds.tinhPhiKinhDoanh() for bds in ds if isinstance(bds, PhiKinhDoanh))
    return tongPhi

def main():
    danhSach = [
    DatTrong("DT001", 50, 20),
    NhaO("NO001", 30, 15, 2),
    KhachSan("KS001", 40, 10, 3),
    BietThu("BT001", 60, 25),
    DatTrong("DT002", 80, 30),
    NhaO("NO002", 70, 20, 3),
    KhachSan("KS002", 90, 15, 5),
    BietThu("BT002", 100, 40),
    DatTrong("DT003", 120, 50),
    NhaO("NO003", 110, 35, 4),
    KhachSan("KS003", 130, 20, 2),
    BietThu("BT003", 140, 45),
    DatTrong("DT004", 150, 55),
    NhaO("NO004", 160, 60, 5),
    ]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu:")  
        print("1. Nhập danh sách bất động sản")
        print("2. Đếm số lượng bất động sản theo từng loại")
        print("3. In danh sách bất động sản có diện tích trên 1000")
        print("4. Tính tổng phí kinh doanh")
        print("5. Thoát")
        choice = input("Chọn chức năng ")
        if choice == '1':
            themBatDongSan(danhSach)
        elif choice == '2':
            demSoLuongTheoLoai(danhSach)
        elif choice == '3':
            inDanhSachDienTichLon(danhSach)
        elif choice == '4':
            tongPhi = tinhTongPhiKinhDoanh(danhSach)
            print(f"Tổng phí kinh doanh: {tongPhi}")
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ !")
        input("Nhan Enter de tiep tuc...")


main()

