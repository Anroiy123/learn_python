'''
Nhập vào thứ trong tuần, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 7) nếu sai yêu cầu nhập lại cho đúng. Khi đã
nhập đúng thì xuất ra tên của thứ trong tuần là tiếng anh.

'''

thu = {
    1 : 'Sunday',
    2 : 'Monday',
    3 : 'Tuesday',
    4 : 'Wednesday',
    5 : 'Thursday',
    6 : 'Friday',
    7 : 'saturday'
}
try: 
    a = int(input('Nhập vào giá trị thứ trong tuần (1,7): '))
    while a not in [1,2,3,4,5,6,7]:
        a = int(input('Nhập lại giá trị thứ trong tuần: '))
except ValueError:
    print('Lỗi nhập định dạng!')

for i in thu:
    if i == a:
        print('thứ trong tuần là:',thu[i])

