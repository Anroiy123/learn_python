def inTenThanhVien(dsNhom):
    print("Danh sach ten thanh vien:")
    for mssv, hoTen in dsNhom.items():
        print(hoTen)

def timTheoMssv(dsNhom, mssvCanTim):
    if mssvCanTim in dsNhom:
        print(f"Tim thay: {dsNhom[mssvCanTim]}")
    else:
        print("Khong tim thay")

def timTheoTen(dsNhom, tenCanTim):
    tenCanTim = tenCanTim.lower()
    timThay = False
    for hoTen in dsNhom.values():
        ten = hoTen.split()[-1].lower()
        if ten == tenCanTim:
            print(f"Tim thay ten {hoTen} trong danh sach")
            timThay = True
    if not timThay:
        print("Khong tim thay ten trong danh sach")


def main():
    dsNhom = {
        "SV001": "Tran Quang Hung",
        "SV002": "Tran Thi Bich",
        "SV003": "Le Van Canh",
        "SV004": "Pham Thi Dung"
    }
    
    print('chọn chức năng:')
    print('1. In danh sách tên thành viên')
    print('2. Tìm theo MSSV')
    print('3. Tìm theo tên')
    print('4. Thoát')

    while True:
        choice = input('Nhập lựa chọn của bạn (1-4): ')
        if choice == '1':
            inTenThanhVien(dsNhom)
        elif choice == '2':
            mssvCanTim = input("Nhap MSSV can tim: ")
            timTheoMssv(dsNhom, mssvCanTim)
        elif choice == '3':
            tenCanTim = input("Nhap ten (khong co ho) can tim: ")
            timTheoTen(dsNhom, tenCanTim)
        elif choice == '4':
            print('Thoát chương trình.')
            break
        else:
            print('Lựa chọn không hợp lệ. Vui lòng thử lại.')

main()