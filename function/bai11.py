'''
Viết hàm giải phương trình bậc hai ax2 + bx + c = 0, với a, b, c là các tham số của hàm. Hàm trả về list chứa các
nghiệm (list rỗng nếu vô nghiệm).
'''

import math
def quadratic_equation(a, b, c):
   if a == 0:
       if b == 0:
           return []
       else:
              return [-c/b]
   delta = pow(b,2) - 4*a*c
   A = []
   if delta < 0:
        return A
   elif delta == 0:
        A.append(((-b)/(2*a)))
   else:
        A.append((-b + math.sqrt(delta))/(2*a))    
        A.append((-b - math.sqrt(delta))/(2*a))
   return A

def main():
   a = float(input(f'nhập vào a: '))
   b = float(input(f'nhập vào b: '))
   c = float(input(f'nhập vào c: '))
   print(f'list chứa các nghiệm là: ', quadratic_equation(a,b,c))

main()
