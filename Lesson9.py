# Quy tắc đặt tên file: [TenLop]_[HoTen]_CP2.py
# Ví dụ: PTB30_BuiDucTrung_CP2.py

# Trong file:

# Trắc nghiệm:
# 1A 2B 3C ....

# Tự luận
# Câu 1:

# Câu 2:
    # Khai báo danh sách ngày trong tuần
weekdays = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"]
    # Khởi tạo danh sách chi tiêu
spends = []

    # Nhập vào số tiền chi tiêu từ t2 - t7
for i in range(6):
    money = float(input(f"Nhập số tiền chi tiêu vào {weekdays[i]}: "))
    spends.append(money)

    # Tính tổng chi tiêu trong tuần
        # Cách 1: DÙng hàm sum() có sẵn
total_spend = sum(spends)
print(f"Tổng chi tiêu trong tuần là: {total_spend} VNĐ")

        # Cách 2:
total_spend = 0
for item in spends:
    total_spend += item
print(f"Tổng chi tiêu trong tuần là: {total_spend} VNĐ")

    # Tìm ngày chi tiêu nhiều nhất
for i in range(len(spends)):
    if spends[i] == max(spends):
        print(f"Ngày chi tiêu nhiều nhất trong tuần là {weekdays[i]} với số tiền {spends[i]} VNĐ")

    # Tính trung bình chi tiêu mỗi ngày
average_spend = total_spend / len(spends)
print(f"Trung bình chi tiêu mỗi ngày trong tuần là: {average_spend} VNĐ")