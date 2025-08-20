# Data types - Kiểu dữ liệu
    # String - Chuỗi ký tự / Xâu ký tự
name = "Tong My Linh"
    # Int (integer): số nguyên
age = 13
    # Float (floating point): số thực
height = 1.65
    # Bool (boolean): kiểu logic, chỉ gồm 2 giá trị True/False
female = True

# Các kiểu print() - 4 kiểu
    # Cách 1: Dùng dấu + 
print("Họ tên: " + name + ' Tuổi: ' + str(age))
    # Cách 2: Dùng dấu ,
print("Chiều cao:", height, 'Nữ:', female)
    # Cách 3: Dùng f - format
print(f"{name} có chiều cao {height}m")
    # Cách 4: in trên nhiều dòng
print(f'''
============ THÔNG TIN =============
Họ tên:     {name}
Tuổi:       {age}
Chiều cao:  {height}m
Nữ:         {female}
====================================''')

# Nhập dữ liệu
name = input("Nhập họ tên: ")
age = int(input("Nhập tuổi: "))
height = float(input("Nhập chiều cao: "))

# Câu điều kiện
    # Các phép so sánh: == != <= >= < >
    # Các phép toán logic: and, or, not
    # Cấu trúc: 3 dạng
        # Dạng thiếu: if ...
        # Dạng đủ: if ... else ...
        # Dạng đa nhánh: if ... elif ... elif ... else ...

# Các phép toán:
    # Thông thường: + - * /
    # Chia lấy dư: %
    # Chia lấy nguyên: //
    # Lũy thừa: **

# Vòng lặp hữu hạn - Vòng lặp for
    # range(start, stop, step)
        # start: số bắt đầu, không bắt buộc, mặc định = 0
        # stop: số kết thúc, bắt buộc
        # step: bước nhảy, không bắt buộc, mặc định = 1
    # Các dạng bài hay gặp: in ra màn hình, tính tổng, đếm

# Vòng lặp vô hạn - Vòng lặp while
    # while <condition>: lặp đến khi điều kiện sai
    # break: thoát khỏi vòng lặp
    # continue: bỏ qua lần lặp hiện tại

# Danh sách - List: CRUD
    # C - Create: Tạo danh sách
        # Tạo danh sách rỗng: PTB30 = []
        # Tạo danh sách có sẵn: numList = [1, 2, 3, 4, 5]
    # R - Read: Đọc / Duyệt danh sách
        # len(): trả về độ dài / số lượng phần tử của danh sách
        # index - chỉ số, value - giá trị
        # arr[0]: phần tử đầu tiên
        # arr[-1]: phần tử cuối cùng
        # Duyệt & in danh sách:
            # cách 1: for i in range(len(arr))
            # cách 2: for item in arr
            # cách 3: for index, value in enumerate(arr)
            # cách 4: print(arr)
    # U - Update: Cập nhật danh sách
        # append(value): thêm phần tử vào cuối danh sách
        # insert(index, value): thêm phần tử vào vị trí chỉ định
        # arr[index] = new_value: chỉnh sửa giá trị phần tử
    # D - Delete: Xóa phần tử
        # remove(value): xóa phần tử theo giá trị
        # pop(index): xóa phần tử theo chỉ số index
        # clear(): xóa toàn bộ phần tử trong danh sách
    # Sắp xếp:
        # sort(): sắp xếp tăng dần
        # sort(reversed=True): sắp xếp giảm dần
    # Khác:
        # min(): tìm giá trị nhỏ nhất
        # max(): tìm giá trị lớn nhất
        # sum(): tính tổng các phần tử

# Chuỗi / Xâu ký tự:
    # len(): độ dài chuỗi
    # strip(): xóa khoảng trắng ở đầu và cuối chuỗi
    # split(): tách chuỗi thành danh sách các phần tử
    # replace(): thay thế một phần của chuỗi
    # upper(): chuyển đổi chuỗi thành chữ hoa
    # lower(): chuyển đổi chuỗi thành chữ thường
    # title(): chuyển đổi chuỗi thành chữ hoa ở đầu mỗi từ

# Hàm / Chương trình con:
    # Hàm không có tham số truyền vào
    # Hàm có tham số truyền vào
    # Hàm có giá trị trả về