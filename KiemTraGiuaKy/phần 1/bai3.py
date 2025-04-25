def nhapDanhSachTraiCay():
    danhSach = []
    print("Nhap danh sach trai cay (nhan Enter de ket thuc):")
    while True:
        ten = input("Nhap ten trai cay (Enter de ket thuc): ").strip()
        if not ten:
            break
        giaTien = float(input("Nhap gia tien ($): "))
        soLuong = int(input("Nhap so luong: "))
        if soLuong <= 0:
            print("So luong phai la so nguyen duong!")
            continue
        traiCay = (ten.lower(), giaTien, soLuong)
        danhSach.append(traiCay)
    return danhSach

def layTenTraiCay(L):
    tenTraiCay = [item[0].upper() for item in L]
    tenTraiCay.sort()
    return tenTraiCay

def tinhTongSoLuong(L):
    tongSoLuong = sum(item[2] for item in L)
    return tongSoLuong

def sapXepTheoSoLuong(L):
    danhSachSapXep = sorted(L, key=lambda x: x[2], reverse=True)
    return danhSachSapXep

def main():
    L = nhapDanhSachTraiCay()
    if not L:
        print("Danh sach rong!")
        return
    
    print("Danh sach vua nhap:", L)
    
    tenTraiCay = layTenTraiCay(L)
    print("a) Danh sach ten trai cay in hoa va sap xep:", tenTraiCay)
    
    tongSoLuong = tinhTongSoLuong(L)
    print("b) Tong so luong trai cay:", tongSoLuong)
    
    danhSachSapXep = sapXepTheoSoLuong(L)
    print("c) Danh sach sap xep theo so luong giam dan:", danhSachSapXep)

main()