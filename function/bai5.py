'''
Viết chương trình kiểm tra xem mật khẩu được khai báo là đạt tính bảo mật cao hay không? 
Mật khẩu được định nghĩa là có tính bảo mật cao khi có ít nhất 8 ký tự đối với độ dài, chứa ít nhất 1 ký tự viết thường,
một ký tự viết hoa,và một con số. Định nghĩa một hàm kiểm tra mật khẩu và hàm này sẽ trả về True nếu mật khẩu thỏa các điều kiện ở
trên. Ngược lại thì hàm sẽ trả về False. Viết chương trình chính (main) để đọc mật khẩu từ người dùng và thông báo
mật khẩu đó có tính bảo mật cao hay không?
'''

def is_high_security(str):
    if len(str) < 8:
        return False
    has_lower = False
    has_upper = False
    has_digit = False

    for char in str:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True

    return has_lower and has_upper and has_digit

def main():
    str = input('nhập vào chuỗi mật khẩu: ')
    if is_high_security(str):
        print('Mật khẩu mạnh')
    else :
        print('Mật khẩu yếu')
    
main()







