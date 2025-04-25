'''
Viết chương trình quản lý thời gian trong ngày sử dụng dictionary với keys là các loại hoạt động (học, ngủ, thể
dục, chơi, di chuyển...) và values là thời gian (theo phút) hoạt động tương ứng. Cần thực hiện chức năng:
a. Nhập thêm thời gian: Hỏi người dùng nhập key hoạt động và số phút rồi cộng dồn vào số phút đang có.
b. Thống kê thời gian các hoạt động (tính theo giờ), ví dụ: Học 8.4 giờ, Ngủ 7.2 giờ, Di chuyển 0.8 giờ...
c. Cho biết 2 hoạt động được làm nhiều nhất và 2 hoạt động làm ít nhất trong ngày.
'''

def add_time(my_dict, activity, time):
    my_dict[activity] = my_dict.get(activity, 0) + time

def convert_to_hour(minutes):
    return minutes / 60

def find_max_min_activities(my_dict):
    sorted_activities = sorted(my_dict.items(), key=lambda x: x[1])
    max_activities = sorted_activities[-2:]
    min_activities = sorted_activities[:2]
    return max_activities, min_activities

n = int(input("Enter the number of activities: "))
mydict = dict()

for i in range(n):
    while True:
        try:
            activity = input(f"Enter the name of activity {i+1}: ")
            if not activity:
                print("Lỗi: Tên hoạt động không được để trống!")
                continue
            time = float(input(f"Enter the time for activity '{activity}' (minutes): "))
            if time < 0:
                print("Lỗi: Thời gian phải lớn hơn hoặc bằng 0!")
                continue
            add_time(mydict, activity, time)
            break
        except ValueError:
            print("Lỗi: Thời gian phải là số hợp lệ (ví dụ: 100, 200.5)!")

print(f"Dictionary: {mydict}")
print("Thống kê thời gian các hoạt động:")
for key, value in mydict.items():
    print(f"{key}: {convert_to_hour(value)} giờ")
max_activities, min_activities = find_max_min_activities(mydict)
print(f"2 hoạt động được làm nhiều nhất: {max_activities}")
print(f"2 hoạt động được làm ít nhất: {min_activities}")
