'''
Nhập vào tháng trong năm, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 12) nếu sai yêu cầu nhập lại cho đúng. Khi
đã nhập đúng thì xuất ra mùa của tháng đã nhập.
'''

def Nhap_thang():
    while True: 
        try: 
            a = int(input('nhập giá trị tháng trong năm [1..12]: '))
            while ( a < 1 ) | ( a > 12 ):
                a = int(input('nhập lại giá trị tháng trong năm [1..12]: '))
            return a
        except ValueError:
            print('Lỗi nhập không đúng định dạng!')

thang = Nhap_thang()

if thang in [1,2,3]:
    mua = 'Xuân'
elif thang in [4,5,6]:
    mua = 'Hạ'
elif thang in [7,8,9]:
    mua = 'Thu'
elif thang in [10,11,12]:
    mua = 'Đông'

print(f'tháng {thang} thuộc mùa {mua}')

