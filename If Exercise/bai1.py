def chuyen_thanh_diem(char):
    if char == 'A+':
        return 4.0
    if char == 'A':
        return 4.0
    if char == 'A-':
        return 3.7
    elif char == 'B+':
        return 3.3
    elif char == 'B':
        return 3.0
    elif char == 'B-':
        return 2.7
    elif char == 'C+':
        return 2.3
    elif char == 'C':
        return 2.0
    elif char == 'C-':
        return 1.7
    elif char == 'D+':
        return 1.3
    elif char == 'D':
        return 1.0
    elif char == 'F':
        return 0.0
    else:
        return -1
    
def main():
    char = input("Nhập ký tự: ")
    score = chuyen_thanh_diem(char)
    while(score == -1):
        char = input("Yêu cầu nhập lại: ")
        score = chuyen_thanh_diem(char)
    print("Điểm số tương ứng: {0}".format(score))

main()
