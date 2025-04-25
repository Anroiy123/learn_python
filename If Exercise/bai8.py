try:
    month = int(input('Nhập giá trị tháng: '))
    if 1<= month <= 12:
        print('tháng bạn vừa nhập hợp lệ')
    else:
        print('tháng bạn vừa nhập không hợp lệ')
    
except:
    print('tháng bạn vừa nhập không hợp lệ')
