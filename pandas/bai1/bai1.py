import pandas as pd
import matplotlib.pyplot as plt
import os

# Lấy đường dẫn thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# a. Đọc dữ liệu từ tập tin, header là row thứ nhất, index là RowNumber
df = pd.read_csv('pandas/Churn_Modelling.csv', header=0, index_col='RowNumber')

# b. Thống kê mô tả các trường
descriptive_stats = df.describe(include='all')

# Ghi thống kê mô tả ra file trong cùng thư mục
descriptive_stats.to_csv(os.path.join(current_dir, 'descriptive_stats.csv'))

# c. Tính trung bình CreditScore theo Geography
credit_score_by_geo = df.groupby('Geography')['CreditScore'].mean()

# Ghi kết quả trung bình CreditScore ra file trong cùng thư mục
credit_score_by_geo.to_csv(os.path.join(current_dir, 'credit_score_by_geography.csv'))

# d. Phân đều Age thành 5 nhóm độ tuổi (mỗi nhóm 20%)
df['AgeGroup'] = pd.qcut(df['Age'], q=5, labels=['Youngest', 'Young', 'Middle', 'Older', 'Oldest'])

# e. Vẽ biểu đồ barchart thống kê số lượng khách hàng theo nhóm độ tuổi
age_group_counts = df['AgeGroup'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
age_group_counts.plot(kind='bar')
plt.title('Number of Customers by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.grid(True, axis='y')

# Lưu biểu đồ trong cùng thư mục
plt.savefig(os.path.join(current_dir, 'age_group_barchart.png'))
plt.close()