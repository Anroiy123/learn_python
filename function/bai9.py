'''
Viết hàm nhận vào một tham số là điện năng tiêu thụ mỗi ngày của một
thiết bị. Hàm in ra thông báo thiết bị có tiết kiệm điện không.
Yêu cầu: hàm này gọi hàm trong câu 2 để tính số sao tiết kiệm. Thiết bị có
số sao nhỏ hơn 3 được gọi là không tiết kiệm điện.

'''

def tinh_so_sao_tiet_kiem(P):
    if P < 2:
        return 5
    elif 2 <= P < 4:
        return 4
    elif 4 <= P < 6:
        return 3
    elif 6 <= P < 10:
        return 2
    elif P >= 10:
        return 1
    else:
        return 0

def kiem_tra_tiet_kiem_dien(P):
    so_sao = tinh_so_sao_tiet_kiem(P)
    if so_sao < 3:
        print("Thiết bị không tiết kiệm điện.")
    else:
        print("Thiết bị tiết kiệm điện.")

def main():
    P = float(input('Nhập vào mức điện năng tiêu thụ : '))
    kiem_tra_tiet_kiem_dien(P)


if __name__ == "__main__":
    main()
    
