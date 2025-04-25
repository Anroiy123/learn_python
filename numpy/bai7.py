import numpy as np

sales = np.random.randint(10, 51, size=(2, 7))

print("Số lượng hàng hóa bán ra trong tuần:")
print(sales)
print()

daily_totals = np.sum(sales, axis=0)
max_day = np.argmax(daily_totals)
print(f"a. Ngày bán được nhiều nhất: Ngày {max_day + 1} với {daily_totals[max_day]} sản phẩm")

max_value = np.max(sales)
max_pos = np.argmax(sales)
max_row, max_col = divmod(max_pos, 7)
time_of_day = "Sáng" if max_row == 0 else "Chiều"
print(f"b. Thời điểm bán nhiều nhất: Buổi {time_of_day}, Ngày {max_col + 1} với {max_value} sản phẩm")

morning_wins = 0
for day in range(7):
    if sales[0, day] > sales[1, day]:
        morning_wins += 1
    elif sales[0, day] < sales[1, day]:
        morning_wins -= 1

if morning_wins > 0:
    print("c. Buổi sáng có khuynh hướng bán được nhiều hàng hơn")
elif morning_wins < 0:
    print("c. Buổi chiều có khuynh hướng bán được nhiều hàng hơn")
else:
    print("c. Cả hai buổi có khuynh hướng bán hàng như nhau")