'''
Cho một list và một tuple, hãy tạo ra kết qủa là tuple và list chứa các phần tử của list và tuple ban đầu.
Ví dụ:
• Input : inputList = [1, 2, 3], inputTuple = (4, 5, 6)
• Output : outputList = [1, 2, 3, 4, 5, 6], outputTuple = (1, 2, 3, 4, 5, 6)
'''
input_l = input('Nhập vào list: ')
lst = [int(x) for x in input_l.split(',')]

input_t = input('Nhập vào tuple: ')
tpl = tuple([int(x) for x in input_t.split(',')])

output_l = lst + list(tpl)
output_t = tuple(lst) + tpl

print(output_l)
print(output_t)