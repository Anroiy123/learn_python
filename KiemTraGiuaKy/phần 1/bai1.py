'''
Bài tập 1. List numbers 1
Viết chương trình xử lý list số theo các yêu cầu sau:
Yêu cầu 1:
- Tạo list số: Cho phép người dùng lần lượt nhập các phần tử số cho list cho đến
khi không muốn nhập nữa.

- Chương trình sẽ :
+ In ra list các số vừa nhập.
+ Tính tổng các phần tử trong list.


Yêu cầu 2:
- Người dùng nhập vào một số x cần tìm
- Chương trình sẽ cho biết :
+ x có xuất hiện trong list hay không? Nếu có thì cho biết x xuất hiện bao nhiêu
lần?
+ x có lớn hơn tất cả các số trong list không?
+ Nếu không thì x nhỏ hơn những số nào trong list? (In ra tất cả các số lớn hơn x)
'''

def TaoListSo():
    ds = []
    print('nhập vào các phần tử (nhấn Enter để kết thúc): ')
    while True:
        value = input('Nhập vào số: ').strip()
        if not value:
            break
        try:     
            num = float(value)
            ds.append(num)
        except ValueError:
            print('vui lòng nhập một số hợp lệ !')
    return ds

def KiemTraListSo(ds):
    if not ds:
        return 'danh sách rỗng!'
    else:
        tong = sum(ds)
        return f'danh sách là {ds} \ncó tổng các phần tử là {tong}'
    
def XuLyTimKiem(ds, x):
    cnt = ds.count(x)
    if cnt:
        print(f'{x} có xuất hiện trong list và xuất hiện {cnt} lần')
    else:
        print(f'{x} không xuất hiện trong danh sách')

    max = all((x > so) for so in ds)
    if max:
        print(f'{x} lớn hơn tất cả các số trong danh sách !')
    else:
        dsLonHon = [i for i in ds if i > x ]
        if dsLonHon:
            print(f'{x} nhỏ hơn các số {dsLonHon}')
        else:
            print(f'không có số nào trong ds lớn hơn {x} (x có thể bằng số lớn nhất)')


def main():
    ds = TaoListSo()
    print(KiemTraListSo(ds))
    while True:
        try:
            x = float(input('nhập vào giá trị x cần tìm: '))
            break
        except ValueError:
            print('Hãy nhập vào 1 số hợp lệ! ')
    XuLyTimKiem(ds, x)

main()

