def chuyen_thanh_diem(char):
    if char == 0.0:
        return 'unacceptable Performance'
    if char == 0.4:
        return 'acceptable Performance'
    if char >= 0.6:
        return 'meritorious Performance'
    else:
        return -1


char = float(input("Nhập giá trị n: "))
score = chuyen_thanh_diem(char)
while(score == -1):
    char = float(input("vui lòng nhập lại: "))
    score = chuyen_thanh_diem(char)
print("Hiệu quả làm việc tương ứng: {0}".format(score))




