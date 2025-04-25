
def nhapSet(tenSet):
    tapHop = set()
    print(f"Nhap cac phan tu so cho {tenSet} (nhan Enter de ket thuc):")
    while True:
        giaTri = input("Nhap so: ").strip()
        if not giaTri:
            break
        try:
            so = float(giaTri)
            tapHop.add(so)
        except ValueError:
            print("Vui long nhap mot so hop le!")
    return tapHop

def xuLySet(set1, set2):
    print("Set1:", set1)
    print("Set2:", set2)
    
    print(f"So phan tu cua Set1: {len(set1)}")
    print(f"Tong gia tri Set1: {sum(set1)}")
    print(f"So phan tu cua Set2: {len(set2)}")
    print(f"Tong gia tri Set2: {sum(set2)}")
    
    print(f"Gia tri lon nhat Set1: {max(set1)}")
    print(f"Gia tri nho nhat Set1: {min(set1)}")
    print(f"Gia tri lon nhat Set2: {max(set2)}")
    print(f"Gia tri nho nhat Set2: {min(set2)}")
    
    phanTu = set1.pop()
    print(f"Phan tu lay ra tu Set1: {phanTu}")
    set1.add(phanTu)
    
    print("Set union cua Set1 va Set2:", set1.union(set2))
    
    print("Set intersection cua Set1 va Set2:", set1.intersection(set2))
    
    print("Set difference cua Set1 voi Set2:", set1.difference(set2))
    
    print("Set symmetric difference cua Set1 va Set2:", set1.symmetric_difference(set2))
    
    print("Set1 sap xep tang dan:", sorted(set1))
    print("Set2 sap xep giam dan:", sorted(set2, reverse=True))

set1 = nhapSet("Set1")
set2 = nhapSet("Set2")
xuLySet(set1, set2)
