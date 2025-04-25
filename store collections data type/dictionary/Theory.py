def Merge(dict1, dict2):
    return dict1 | dict2

dict1 = { 'x' : 10, 'y' : 8 }
dict2 = { 'a' : 6, 'b' : 4 }
dict3 = Merge(dict1, dict2)
print(dict3) 
print(len(Merge(dict1, dict2)))
print(dict3.get('a')) # trả về value theo keys đc nhập vào
print(dict3.keys()) # trả về các key
print(dict1.values()) # trả về các giá trị
print(dict2.items()) # trả về các cặp giá trị
dict3['c'] = '2' # thay đổi giá trị
print(dict3)
dict3.update({'c' : 8}) # thay đổi hoặc thêm giá trị 
print(dict3)
dict3['d'] = 10 # thêm giá trị
print(dict3)
dict3.pop('d') # xoá phần tử theo keys được nhập vào
print(dict3)
dict3.popitem() # xoá phần tử cuối cùng
print(dict3)
del dict3['b'] # xoá phần tử theo keys được nhập vào
print(dict3)
dict4 = dict3.copy() # copy từ điển
dict5 = dict(dict4) # copy từ điển
dict6 = dict1 | dict2 # hợp nhất 2 từ điển
dict3.clear() # xoá toàn bộ phần tử trong từ điển
print(dict3)
print(dict4)
print(dict5)
del dict3 # xoá hoàn toàn dictionary . Lưu ý : khi đã xoá rồi thì khi print ra sẽ báo lỗi
if 'a' in dict2:
    print('yes, a is one of the \'key\' in the dict2 dictionary')
for i in dict1:
    print(i, ":",dict1[i]) 
for i in dict1.values():
    print(i, end=' ');print()
for x,y in dict1.items():
    print(x,y)
