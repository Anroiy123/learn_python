'''
Biến đoạn code viết hoa các chữ cái đầu từ trong tuần 7 thành một hàm nhận vào một string và trả về một
string đã được viết hoa các chữ cái đầu từ. Ví dụ: “nGuyeN hiEu NGhiA” → “Nguyen Hieu Nghia”.
'''

def capitalize_first_letter(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result

def main():
    input_string = input("Nhập chuỗi cần viết hoa chữ cái đầu: ")
    output_string = capitalize_first_letter(input_string)
    print("Chuỗi đã được viết hoa chữ cái đầu:", output_string)


main()