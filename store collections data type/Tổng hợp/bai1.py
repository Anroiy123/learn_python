'''
Mã Morse là một sơ đồ mã hóa sử dụng dấu - và dấu . để thể hiện các số và ký tự. Viết chương trình sử dụng
dictionary để lưu trữ bảng ánh xạ các ký tự này sang mã Morse. Bảng ánh xạ được thể hiện dưới đây. Chương
trình sẽ đọc một chuỗi từ người dùng sau đó sẽ dịch chuỗi gồm các ký tự và số thành mã Morse, đặt thêm các
khoảng trắng giữa chuỗi các dấu gạch ngang - và dấu chấm .
Chương trình sẽ bỏ qua bất cứ ký tự
nào không được liệt kê ở bảng bên.
Dưới đây là mã Morse cho chuỗi
Hello, World!: .... . .-.. .-.. --- .-- --- .-. .-.. -..
'''

def morse_code(s):
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    return ' '.join([morse[c] for c in s.upper() if c in morse])

s = input("Enter a string: ")
print(f"Mã Morse của chuỗi '{s}' là: {morse_code(s)}")

