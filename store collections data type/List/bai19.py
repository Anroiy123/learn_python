'''
  (Change coin) Với một giá trị N, nếu chúng ta muốn đổi N xu và chúng ta có nguồn cung vô hạn đối với mỗi
đồng xu có giá trị S = { S1, S2, … Sm }. Hỏi có thể thực hiện bao nhiêu cách để thực hiện thay đổi? 
(thứ tự các đồng xu là không quan trọng). 
Ví dụ:
Với N = 04 và S = { 1, 2, 3 } , có 04 nghiệm : { 1, 1, 1, 1 }, { 1, 1, 2 }, { 2, 2 }, { 1, 3 }.
Với N = 10 và S = { 2, 5, 3, 6 } , có 05 nghiệm : { 2, 2, 2, 2, 2 }, { 2, 2, 3, 3 }, { 2, 2, 6 }, { 2, 3, 5 }, { 5, 5 }
'''

def dem_cach_doi_tien(N, S):
    # Khởi tạo mảng dp để lưu số cách đổi cho từng giá trị từ 0 đến N
    dp = [0] * (N + 1)
    dp[0] = 1  # Có 1 cách đổi 0 xu (không dùng đồng xu nào)

    # Duyệt qua từng đồng xu trong S
    for coin in S:
        # Cập nhật dp cho từng giá trị từ coin đến N
        for amount in range(coin, N + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[N]

def in_cach_doi_tien(N, S):
    # Tạo danh sách lưu các cách đổi (tùy chọn, để minh họa)
    def tim_cach(N, S, start, current, results):
        if N == 0:
            results.append(sorted(current[:]))  # Sắp xếp để loại bỏ thứ tự
            return
        if N < 0:
            return
        for i in range(start, len(S)):
            if S[i] <= N:
                current.append(S[i])
                tim_cach(N - S[i], S, i, current, results)
                current.pop()

    results = []
    tim_cach(N, S, 0, [], results)
    return results

# Chương trình chính
def main():
    # Nhập giá trị N
    while True:
        try:
            N = int(input("Nhập giá trị N (số xu cần đổi, N > 0): "))
            if N <= 0:
                print("Lỗi: N phải lớn hơn 0. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

    # Nhập danh sách các giá trị đồng xu S
    while True:
        try:
            input_S = input("Nhập các giá trị đồng xu (cách nhau bởi khoảng trắng, số nguyên dương): ")
            S = [int(x) for x in input_S.split()]
            if not S or any(x <= 0 for x in S):
                print("Lỗi: Các giá trị đồng xu phải là số nguyên dương. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập các số nguyên hợp lệ!")

    # Tính số cách đổi
    so_cach = dem_cach_doi_tien(N, S)
    print(f"Số cách đổi {N} xu bằng các đồng xu {S} là: {so_cach}")

    # In các cách đổi (tùy chọn, để minh họa)
    cach_doi = in_cach_doi_tien(N, S)
    if len(cach_doi) > 0:
        print("Các cách đổi cụ thể (tập hợp các đồng xu, không xét thứ tự):")
        for i, cach in enumerate(cach_doi, 1):
            print(f"Cách {i}: {cach}")

if __name__ == "__main__":
    main()