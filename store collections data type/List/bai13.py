'''
Viết chương trình cho phép nhập một list có n phần tử số nguyên (n≥0) và giá trị k (k≥0). Hãy tìm trong list
những ước số và bội số của k (nếu có).
'''
def is_conven(num,k):
    return k % num == 0 if num != 0 else False

def is_multiple(num,k):
    return num % k == 0 if k != 0 else False

n = int(input('Nhập vào số lượng phần tử n(n>=0): '))
A = []
for i in range(n): 
    A.append(int(input('Nhập vào giá trị thứ {0}: '.format(i+1))))

k = int(input('Nhập vào giá trị k(k>=0): '))
conven = []
multiple = []

print(A)
for i in A:
    if is_conven(i, k):
        conven.append(i)
    if is_multiple(i,k):
        multiple.append(i)

if not conven:
    print('không có ước số nào!')
else:
    print(f'{k} có những ước số là: ',conven)

if not multiple:
    print('không có bội số nào!')
else:
    print(f'{k} có những bội số là: ',multiple)

