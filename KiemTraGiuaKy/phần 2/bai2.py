import os 
from datetime import datetime

class DiaChi:
    def __init__(self, soNha, tenDuong, tenQuan, thanhPho):
        self.soNha = soNha
        self.tenDuong = tenDuong
        self.tenQuan = tenQuan
        self.thanhPho = thanhPho

    def inThongTin(self):
        print(f'Địa chỉ là: {self.soNha}, {self.tenDuong}, {self.tenQuan}, {self.thanhPho}')

class NhanVien:
    def __init__(self, hoTen, ngaySinh, diaChi):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diaChi = diaChi
    
    def inThongTin(self):
        print(f'Họ và tên: {self.hoTen}')
        print(f'Ngày sinh: {self.ngaySinh.strftime('%d/%m/%Y')}')
        self.diaChi.inThongTin()
    

class NhanVienSanXuat(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, luongCB, soSP):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.luongCB = luongCB
        self.soSP = soSP

    def TinhLuong(self):
        return self.luongCB + self.soSP * 5000
    
    def inThongTin(self):
        super().inThongTin()
        print('loại nhân viên: Sản xuất')
        print(f'lương cơ bản: {self.luongCB}')
        print(f'số sản phẩm: {self.soSP}')
        print(f'Tổng lương: {self.TinhLuong()}')

class NhanVienVanPhong(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, soNgayLamViec : int):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.soNgayLamViec = soNgayLamViec
    
    def TinhLuong(self):
        return self.soNgayLamViec * 100000
    
    def inThongTin(self):
        super().inThongTin()
        print('Loại nhân viên: Văn phòng')
        print(f'Số ngày làm việc: {self.soNgayLamViec}')
        print(f'Tổng lương: {self.TinhLuong()}')

def TaoDiaChi():
    soNha = input('Nhập số nhà: ')
    tenDuong = input('Nhập tên đường: ')
    tenQuan = input('Nhập tên quận: ')
    thanhPho = input('Nhập tên thành phố: ')
    diaChi = DiaChi(soNha, tenDuong, tenQuan, thanhPho)
    return diaChi

def themNhanVienSanXuat():
    hoTen = input('Nhập họ tên nhân viên sản xuất: ')
    ngaySinh = datetime.strptime(input('Nhập ngày sinh (dd-mm-yyyy): '), '%d/%m/%Y')
    diaChi = TaoDiaChi()
    luongCB = float(input('Nhập lương cơ bản: '))
    soSP = int(input('Nhập số sản phẩm: '))
    nvSanXuat = NhanVienSanXuat(hoTen, ngaySinh, diaChi, luongCB, soSP)
    return nvSanXuat

def themNhanVienVanPhong():
    hoTen = input('Nhập họ tên nhân viên văn phòng: ')
    ngaySinh = datetime.strptime(input('Nhập ngày sinh (dd-mm-yyyy): '), '%d/%m/%Y')
    diaChi = TaoDiaChi()
    soNgayLamViec = int(input('Nhập số ngày làm việc: '))
    nvVanPhong = NhanVienVanPhong(hoTen, ngaySinh, diaChi, soNgayLamViec)
    return nvVanPhong



def main():
    danhSachNVSanXuat = []
    danhSachNVVanPhong = []

    # Tạo một số nhân viên mẫu
    diaChi1 = DiaChi("123", "Duong A", "Quan 1", "HCM")
    diaChi2 = DiaChi("456", "Duong B", "Quan 2", "HCM")
    diaChi3 = DiaChi("789", "Duong C", "Quan 3", "HCM")

    nvSanXuat1 = NhanVienSanXuat("Nguyen Van A", datetime(1990, 5, 15), diaChi1, 5000000, 100)
    nvSanXuat2 = NhanVienSanXuat("Tran Thi B", datetime(1992, 8, 20), diaChi2, 6000000, 80)
    nvVanPhong1 = NhanVienVanPhong("Le Van C", datetime(1995, 3, 10), diaChi3, 20)
    nvVanPhong2 = NhanVienVanPhong("Nguyen Thi D", datetime(1993, 7, 25), diaChi1, 15)

    danhSachNVSanXuat.append(nvSanXuat1)
    danhSachNVSanXuat.append(nvSanXuat2)
    danhSachNVVanPhong.append(nvVanPhong1)
    danhSachNVVanPhong.append(nvVanPhong2)
    


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Chương trình quản lý nhân viên')
        print('1. Thêm nhân viên sản xuất')
        print('2. Thêm nhân viên văn phòng')
        print('3. In thông tin nhân viên sản xuất')
        print('4. In thông tin nhân viên văn phòng')
        print('5. Thoát')

        luaChon = input('Nhập lựa chọn của bạn: ')
        
        if luaChon == '1':
            nvSanXuat = themNhanVienSanXuat()
            danhSachNVSanXuat.append(nvSanXuat)
        
        elif luaChon == '2':
            nvVanPhong = themNhanVienVanPhong()
            danhSachNVVanPhong.append(nvVanPhong)
        
        elif luaChon == '3':
            for nv in danhSachNVSanXuat:
                nv.inThongTin()
                print('-' * 20)
        
        elif luaChon == '4':
            for nv in danhSachNVVanPhong:
                nv.inThongTin()
                print('-' * 20)
        
        elif luaChon == '5':
            break
        
        else:
            print('Lựa chọn không hợp lệ!')
        input('Nhấn Enter để tiếp tục...')


main()