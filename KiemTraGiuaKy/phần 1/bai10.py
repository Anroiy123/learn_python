def taoTuDienNam():
    can = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
    chi = ["Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui", "Than", "Dau", "Tuat", "Hoi"]
    tuDienNam = {}
    for nam in range(2020, 2080):
        viTriCan = (nam - 2020) % 10
        viTriChi = (nam - 2020) % 12
        tenNamAmLich = f"{can[viTriCan]} {chi[viTriChi]}"
        tuDienNam[nam] = tenNamAmLich
    return tuDienNam

def inDanhSachNam(tuDienNam):
    print("Danh sach 60 nam am lich tu 2020 den 2079:")
    for nam in range(2020, 2080):
        print(f"{nam} la nam {tuDienNam[nam]}", end=", " if nam < 2079 else "\n")
        print()

def timNamAmLich(tuDienNam, namDuongLich):
    if namDuongLich in tuDienNam:
        print(f"Nam {namDuongLich} la nam {tuDienNam[namDuongLich]}")
    else:
        print("Nam nhap vao khong nam trong khoang 2020-2079!")

def main():
    tuDienNam = taoTuDienNam()
    inDanhSachNam(tuDienNam)
    namDuongLich = int(input("Nhap nam duong lich can tim: "))
    timNamAmLich(tuDienNam, namDuongLich)

main()