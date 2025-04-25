
def taoTuDienKhoa(L):
    tuDienKhoa = {}
    for chuoi in L:
        tenKhoa, khoaHoc, soLuong = chuoi.split(',')
        tuDienKhoa[tenKhoa] = int(soLuong)
    return tuDienKhoa

def tinhTongSoLuong(tuDienKhoa):
    return sum(tuDienKhoa.values())

def timKhoaLonNhat(tuDienKhoa):
    khoaLonNhat = max(tuDienKhoa, key=tuDienKhoa.get)
    return khoaLonNhat


L = ["CNTT,20,600", "Ly,18,200", "Toan,19,100", "Hoa,19,150"]
print("Danh sach ban dau:", L)

tuDienKhoa = taoTuDienKhoa(L)
print("a) Tu dien khoa:", tuDienKhoa)

tongSoLuong = tinhTongSoLuong(tuDienKhoa)
print("b) Tong so luong sinh vien:", tongSoLuong)

khoaLonNhat = timKhoaLonNhat(tuDienKhoa)
print("c) Khoa co so luong sinh vien lon nhat:", khoaLonNhat)

