'''
Viết hàm nhận vào một tham số là điện năng tiêu thụ mỗi ngày của một thiết bị. Hàm kiểm tra thiết bị này có
tiết kiệm điện hay không và in ra thông báo. Biết rằng nếu điện năng tiêu thụ mỗi ngày < 10 kWh được gọi là tiết
kiệm
'''

def kiem_tra_tiet_kiem_dien(dien_nang_tieu_thu):
    if dien_nang_tieu_thu < 10:
        return "Thiết bị này tiết kiệm điện."
    else:
        return "Thiết bị này không tiết kiệm điện."
    

def main():
    dien_nang_tieu_thu = float(input("Nhập điện năng tiêu thụ mỗi ngày của thiết bị (kWh): "))
    # kiểm tra điện năng tiêu thụ
    result = kiem_tra_tiet_kiem_dien(dien_nang_tieu_thu)
    print(result)

main()





















    


