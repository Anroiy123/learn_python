def xuLyChuoi(chuoi):
    danhSachTu = chuoi.split()
    print(f'danh sách từ : {danhSachTu}')
    tapHopTu = set(danhSachTu)
    danhSachSapXep = sorted(tapHopTu)
    ketQua = " ".join(danhSachSapXep)
    return ketQua

chuoiNhap = input("Nhap chuoi: ")
print("Chuoi sau khi xu ly:", xuLyChuoi(chuoiNhap))
