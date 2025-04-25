'''
Viết chương trình tính giá tiền dịch vụ taxi. Giá thành dịch vụ taxi bao gồm chi phí cơ sở là 4USD và cộng thêm
0.25USD cho mỗi 140m di chuyển. Viết một chương trình có đầu vào là quãng đường di chuyển (tính theo km)
sau đó trả về giá dịch vụ cho quãng đường đó. Viết một chương trình chính (main) để minh họa hàm vừa xây
dựng. Lưu ý: vì giá vé có thể thay đổi, hãy định nghĩa một hằng số qui định giá cơ sở để có thể linh hoạt cho các
trường hợp giá thành tăng.
'''

def taxi_service(distance_km):
    BASE_COST = 4.0  
    COST_PER_140M = 0.25  
    distance_m = distance_km * 1000
    num_segments = distance_m // 140
    total_cost = BASE_COST + (num_segments * COST_PER_140M)

    return total_cost


def main():
    distance_km = float(input("Nhập quãng đường di chuyển (km): "))
    cost = taxi_service(distance_km)

    print(f"Giá dịch vụ taxi cho quãng đường {distance_km} km là: {cost:.2f} USD")

main()




