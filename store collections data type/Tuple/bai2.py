'''
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là
number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là: Sắp xếp theo name > age > score. Ví dụ:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
➔ [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

n = int(input('Nhập vào số lượng tuple: '))
lst = []
for i in range(n):
    tpl = tuple(input(f'Nhập vào tuple thứ {i+1}: ').split(','))
    lst.append(tpl)
    
lst.sort(key=lambda x: x)
print(lst)

