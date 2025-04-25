'''
3. Sử dụng bộ dữ liệu u.user thực hiện các yêu cầu sau:
a. Đọc dữ liệu từ tập tin đã cho
b. Cho biết độ tuổi trung bình của mỗi nghề nghiệp
c. Cho biết tỷ lệ năm trên mỗi nghề và sắp xếp từ cao đến thấp
d. Với mỗi nghề nghiệp, hãy cho biết độ tuổi nhỏ nhất và lớn nhất
e. Với mỗi tổ hợp của nghề nghiệp - giới tính, hãy tính tuổi trung bình
f. Với mỗi nghề nghiệp, hãy cho biết tỷ lệ phần trăm của nam - nữ
'''

import pandas as pd

# a. Đọc dữ liệu từ tập tin u.user
# File u.user thường không có header, các cột là: user_id, age, gender, occupation, zip_code
df = pd.read_csv('u.user', sep='|', header=None, names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])

# b. Độ tuổi trung bình của mỗi nghề nghiệp
avg_age_by_occupation = df.groupby('occupation')['age'].mean().round(2)

# Ghi kết quả ra file
avg_age_by_occupation.to_csv('pandas/bai3/avg_age_by_occupation.csv')

# c. Tỷ lệ nam trên mỗi nghề, sắp xếp từ cao đến thấp
# Giả sử gender: M = Male, F = Female
male_ratio = df[df['gender'] == 'M'].groupby('occupation').size() / df.groupby('occupation').size()
male_ratio = male_ratio.round(2).sort_values(ascending=False)

# Ghi kết quả ra file 
male_ratio.to_csv('male_ratio_by_occupation.csv')

# d. Độ tuổi nhỏ nhất và lớn nhất của mỗi nghề nghiệp
age_min_max = df.groupby('occupation')['age'].agg(['min', 'max'])

# Ghi kết quả ra file
age_min_max.to_csv('age_min_max_by_occupation.csv')

# e. Tuổi trung bình của mỗi tổ hợp nghề nghiệp - giới tính
avg_age_by_occupation_gender = df.groupby(['occupation', 'gender'])['age'].mean().round(2)

# Ghi kết quả ra file
avg_age_by_occupation_gender.to_csv('avg_age_by_occupation_gender.csv')

# f. Tỷ lệ phần trăm nam - nữ của mỗi nghề nghiệp
gender_counts = df.groupby(['occupation', 'gender']).size().unstack(fill_value=0)
gender_percentage = (gender_counts.div(gender_counts.sum(axis=1), axis=0) * 100).round(2)

# Ghi kết quả ra file
gender_percentage.to_csv('gender_percentage_by_occupation.csv')


