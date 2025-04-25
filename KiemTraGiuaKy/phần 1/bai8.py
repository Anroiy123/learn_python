import os

    

def timLienHe(danhBa, searchName):
    if searchName in danhBa:
        print(f"Tim thay: {searchName} - {danhBa[searchName]}")
    else:
        print("Khong tim thay lien he!")

def themLienHe(danhBa, ten, soDienThoai):
    danhBa[ten] = soDienThoai
    print(f"Da them lien he: {ten} - {soDienThoai}")

def inDanhBa(danhBa):
    print("Danh ba dien thoai:")
    for ten, soDienThoai in danhBa.items():
        print(f"{ten}: {soDienThoai}")

def main():
    danhBa = {
        "Johnny": "0989741258",
        "Katherine": "0903852147",
        "Misu": "0913753951",
        "Jack": "0933753654"
    }
    
    while True:
        os.system('cls')
        print("Chuc nang:")
        print("1. Tim lien he")
        print("2. Them lien he")
        print("3. In danh ba")
        print("4. Thoat")
        chucNang = int(input("Chon chuc nang (1-4): "))
        print("---------------")
        if chucNang == 1:
            searchName = input("Nhap ten lien he can tim: ")
            timLienHe(danhBa, searchName)
        elif chucNang == 2:
            ten = input("Nhap ten lien he: ")
            soDienThoai = input("Nhap so dien thoai: ")
            themLienHe(danhBa, ten, soDienThoai)
        elif chucNang == 3:
            inDanhBa(danhBa)
        elif chucNang == 4:
            print("Thoat chuong trinh.")
            break
        else:
            print("Chuc nang khong hop le!") 
        print("---------------")
        os.system('pause')
            
main()