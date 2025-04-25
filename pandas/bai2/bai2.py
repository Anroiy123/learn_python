'''
2. Sử dụng bộ dữ liệu chipotle.tsv thực hiện các yêu cầu sau:
a. Đọc dữ liệu từ tập tin đã cho
b. Liệt kê những sản phẩm có giá hơn 10$ (lược bỏ những dòng trùng tên sản phẩm)
c. Sắp xếp các sản phẩm theo tên
d. Tìm sản phẩm có giá cao nhất trong danh sách
e. Cho biết sản phẩm “Veggie Salad Bowl” xuất hiện trong bao nhiêu đơn hàng với tổng số lượng được đặt
f. Vẽ biểu đồ histogram cho 5 sản phẩm được mua nhiều nhất với tần suất mua
g. Vẽ biểu đồ scatter với số lượng mặt hàng được đặt hàng trên mỗi đơn hàng
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

# Get current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# a. Đọc dữ liệu từ tập tin chipotle.tsv với đường dẫn đầy đủ
df = pd.read_csv(os.path.join(current_dir, 'chipotle.tsv'), sep='\t')

# Fix invalid escape sequence by using raw string
df['item_price'] = df['item_price'].replace(r'[$,]', '', regex=True).astype(float)

# b. Liệt kê những sản phẩm có giá hơn 10$, lược bỏ trùng lặp
unique_items = df[['item_name', 'item_price']].drop_duplicates()
expensive_items = unique_items[unique_items['item_price'] > 10][['item_name', 'item_price']]

# Ghi danh sách sản phẩm đắt tiền ra file
expensive_items.to_csv('expensive_items.csv', index=False)

# c. Sắp xếp các sản phẩm theo tên
sorted_items = expensive_items.sort_values(by='item_name')

# Ghi danh sách đã sắp xếp ra file
sorted_items.to_csv('sorted_expensive_items.csv', index=False)

# d. Tìm sản phẩm có giá cao nhất
max_price_item = df.loc[df['item_price'].idxmax(), ['item_name', 'item_price']]

# Ghi sản phẩm giá cao nhất ra file
with open('max_price_item.txt', 'w') as f:
    f.write(f"Item: {max_price_item['item_name']}, Price: ${max_price_item['item_price']}")

# e. Số đơn hàng và tổng số lượng của "Veggie Salad Bowl"
veggie_orders = df[df['item_name'] == 'Veggie Salad Bowl']
num_orders = veggie_orders['order_id'].nunique()
total_quantity = veggie_orders['quantity'].sum()

# Ghi kết quả Veggie Salad Bowl ra file
with open('veggie_salad_bowl.txt', 'w') as f:
    f.write(f"Veggie Salad Bowl appears in {num_orders} orders with total quantity {total_quantity}")

# f. Vẽ biểu đồ bar chart (thay vì histogram) cho 5 sản phẩm được mua nhiều nhất
top_5_items = df.groupby('item_name')['quantity'].sum().nlargest(5)
plt.figure(figsize=(12, 6))
top_5_items.plot(kind='bar')  # Thay đổi từ 'hist' sang 'bar'
plt.title('Top 5 Most Purchased Items')
plt.xlabel('Item Name')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45, ha='right')  # Xoay nhãn để dễ đọc
plt.tight_layout()  # Điều chỉnh layout để tránh cắt nhãn

# Lưu biểu đồ bar chart
plt.savefig('top_5_items_barchart.png')
plt.close()

# g. Vẽ biểu đồ scatter cho số lượng mặt hàng trên mỗi đơn hàng
items_per_order = df.groupby('order_id')['quantity'].sum()
plt.figure(figsize=(12, 6))
plt.scatter(range(len(items_per_order)), items_per_order.values, alpha=0.5)  # Sử dụng range thay vì index
plt.title('Number of Items per Order')
plt.xlabel('Order Index')  # Thay đổi nhãn phù hợp hơn
plt.ylabel('Total Quantity')
plt.grid(True)
plt.tight_layout()

# Lưu biểu đồ scatter
plt.savefig('items_per_order_scatter.png')
plt.close()