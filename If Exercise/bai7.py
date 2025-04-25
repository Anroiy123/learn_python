year = int(input('Nhập số năm: '))
thu = {
    0 : 'chủ nhật',
    1 : 'thứ hai',
    2 : 'thứ ba',
    3 : 'thứ tư',
    4 : 'thứ năm',
    5 : 'thứ sáu',
    6 : 'thứ bảy'
}

a = (year + ((year-1)//4) - ((year-1) // 100) + ((year - 1) // 400)) % 7

print('thứ của ngày đầu tiên trong năm',year,'là :', thu[a])

