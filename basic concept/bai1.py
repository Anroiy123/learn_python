'''
Viết chương trình cho phép người dùng nhập vào số lượng và đơn giá của một sản phẩm. Xuất lên màn hình
tổng tiền trước thuế, tiền thuế 10%, tổng tiền sau thuế. Mức thuế cần khai báo là hằng số
'''

n = int(input("Nhập đơn giá: "))
m = int(input("Nhập số lượng: "))
tong_tien_truoc_thue = n * m
thue = 0.1
tien_thue = tong_tien_truoc_thue * thue
tong_tien_sau_thue = tong_tien_truoc_thue + tien_thue
print(f"Tổng tiền trước thuế: {tong_tien_truoc_thue}")
print(f"Tiền thuế 10%: {tien_thue}")
print(f"Tổng tiền sau thuế: {tong_tien_sau_thue}")


