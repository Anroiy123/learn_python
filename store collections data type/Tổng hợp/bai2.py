'''
Đếm số lần xuất hiện của các chữ cái (không kể dấu câu, ví dụ: .,-) được dùng trong một câu. Ví dụ:
“An eye for an eye makes the whole world blind. - Mahatma Gandhi”1
Câu này có số lần xuất hiện của 'A': 1 lần, 'a': 6 lần, 'b': 1 lần...
Gợi ý: Có thể dùng set và dictionary kết hợp với vòng lặp để đếm (dictionary dùng để lưu kết quả)
'''

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
letter_count = dict()

for letter in sentence:
    if letter.isalpha():
        letter_count[letter] = letter_count.get(letter, 0) + 1

print("Số lần xuất hiện của các chữ cái trong câu:")
for letter, count in letter_count.items():
    print(f"{letter}: {count} lần")

    