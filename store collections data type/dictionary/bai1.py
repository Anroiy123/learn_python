'''
(Merge dictionary) Cho 2 dictionary, hãy tạo thành một dictionary là merge của 2 dictionary này. Ví dụ:
dict1 = { 'x' : 10, 'y' : 8 }
dict2 = { 'a' : 6, 'b' : 4 }
dict3 = Merge(dict1, dict2) ➔ dict3 = { 'x' : 10, 'y' : 8, 'a' : 6, 'b' : 4 }
'''
def Merge(dict1, dict2):
    return dict1 | dict2

dict1 = { 'x' : 10, 'y' : 8 }
dict2 = { 'a' : 6, 'b' : 4 }
dict3 = Merge(dict1,dict2)
print(dict3)
