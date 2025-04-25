'''
Viết hàm nhận vào một tham số là điện năng tiêu thụ mỗi ngày của một thiết bị. Hàm trả về số sao tiết kiệm
năng lượng của thiết bị, với số sao tiết kiệm được quy định như hình bên
'''


def kiem_tra_tiet_kiem_dien(P):
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
    

P = float(input('Nhập vào mức điện năng tiêu thụ : '))
result = kiem_tra_tiet_kiem_dien(P)
print(result)




