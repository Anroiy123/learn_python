import math

def laSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def taoDanhSachSo():
    danhSachSo = []
    print("Nhap cac phan tu so vao danh sach (nhan Enter de ket thuc):")
    while True:
        giaTri = input("Nhap so: ").strip()
        if not giaTri:
            break
        try:
            so = float(giaTri)
            danhSachSo.append(so)
        except ValueError:
            print("Vui long nhap mot so hop le!")
    return danhSachSo

def xuLyDanhSachSo(danhSachSo):
    if not danhSachSo:
        print("Danh sach rong!")
        return
    
    print(f"Danh sach vua nhap: {danhSachSo}")
    
    soNguyenTo = [x for x in danhSachSo if x.is_integer() and laSoNguyenTo(int(x))]
    if soNguyenTo:
        print(f"Cac so nguyen to trong danh sach: {soNguyenTo}")
    else:
        print("Khong co so nguyen to nao trong danh sach!")
    
    soAm = [x for x in danhSachSo if x < 0]
    if soAm:
        trungBinhAm = sum(soAm) / len(soAm)
        print(f"Trung binh cong cac so am: {trungBinhAm:.2f}")
    else:
        print("Khong co so am nao trong danh sach!")
    
    soDuong = [x for x in danhSachSo if x > 0]
    if soDuong:
        trungBinhDuong = sum(soDuong) / len(soDuong)
        print(f"Trung binh cong cac so duong: {trungBinhDuong:.2f}")
    else:
        print("Khong co so duong nao trong danh sach!")
    
    soChan = [x for x in danhSachSo if x.is_integer() and int(x) % 2 == 0]
    if soChan:
        chanLonNhat = max(soChan)
        print(f"Gia tri chan lon nhat: {chanLonNhat}")
    else:
        print("Khong co gia tri chan nao trong danh sach!")
    
    soLe = [x for x in danhSachSo if x.is_integer() and int(x) % 2 != 0]
    if soLe:
        leNhoNhat = min(soLe)
        print(f"Gia tri le nho nhat: {leNhoNhat}")
    else:
        print("Khong co gia tri le nao trong danh sach!")
    
    danhSachSapXep = sorted(danhSachSo)
    print(f"Danh sach sau khi sap xep tang dan: {danhSachSapXep}")


#main
danhSachSo = taoDanhSachSo()
xuLyDanhSachSo(danhSachSo)