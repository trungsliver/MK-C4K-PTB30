# Quy tắc đặt tên biến
    # Chỉ gồm chữ cái tiếng Anh, số, ký tự gạch dưới
    # Không bắt đầu bằng số
    # Phân biệt chữ hoa và chữ thường
    # Không dùng từa khóa để đặt tên biến

# Ví dụ:
    # Tên sai: 2nd_place (second_place), class, first-name (first_name), user@home, def
    # Tên đúng: age, _username, isValid, total_1

# Quy tắc đặt tên biến dài
    # Dạng snake_case
        # Ví dụ: first_name, last_name, full_name, is_valid, has_children, ...

    # Dạng camelCase
        # Ví dụ: firstName, lastName, fullName, isValid, ...

# Toán tử số học (operators)
    # Cơ bản: + - * /
    # Chia lấy dư: %
print('7 % 3 =', 7%3)       # Output: 7 % 3 = 1
    # Chia lấy nguyên: //
print('7 // 3 =', 7//3)     # Output: 7 // 3 = 2
    # Lũy thừa: ** (thực hiện từ phải -> trái)
print('2**2**3 = 2**(2**3) = 2**8 =', 2**2**3)

    # Thứ tự thực hiện: Lũy thừa => Nhân chia => Cộng trừ
    # Lưu ý: Nếu biểu thức lũy thừa nhiều hơn 2 số, tính từ phải sang trái
        # Ví dụ: 2**2**3 = 2**(2**3) = 2**8
print('1 + 1 =', 1+1)

    # Toán tử số học với string
        # Phép nối: +
print('Đức' + ' ' + 'Trung')   # Output: Đức Trung
        # Phép lặp lại: *
print('hi' * 3)                 # Output: hihihi
print('Linh' * 0)               # Output: 

    # Bài tập: Nhập a là chiều dài của cạnh hình vuông.
    # Tính chu vi, diện tích hình vuông và hiển thị ra màn hình.

    # START
        # INPUT a
        # SET cvi TO a * 4
        # SET dtich TO a * a
        # OUTPUT 'Chu vi:' + cvi
        # OUTPUT 'Diện tích:' + dtich
    # END

    # Bước 1: Nhập chiều cạnh
a = float(input('Nhập chiều dài cạnh hình vuông: '))
    # Bước 2: Tính chu vi, diện tích HCN
cvi = a * 4
dtich = a * a
    # Bước 3: Hiển thị kết quả
print('Chu vi hình vuông:', cvi)
print('Diện tích hình vuông:', dtich)

# Toán tử quan hệ (relational operators)
    # So sánh bằng (equal to): ==
print(5 == 5)           # Output: True
print(5 == 3)           # Output: False
    # So sánh khác (not equal to): !=
print(5 != 5)           # Output: False
print(5 != 3)           # Output: True
    # So sánh lớn hơn / nhỏ hơn (greater than / less than): > < >= <=
print(5 >= 5)           # Output: True
print(5 < 3)            # Output: False

# Toán tử logic (Logical operators): AND - OR - NOT
    # Ví dụ: trà sữa - gà rán

# Biểu thức logic (Logical expressions)

# Câu điều kiện (If-else statements / Conditional statements)
    # Dạng thiếu (single condition)
age = int(input('Nhập tuổi của bạn: '))
if age >= 18:
    print('Bạn đã đủ 18 tuổi')  
    print('Bạn đã là người trưởng thành')

    # Dạng đủ (two-way condition)
score = 8
if score >= 5:
    print('Bạn đã đạt yêu cầu')
else:
    print('Bạn chưa đạt yêu cầu')

    # Dạng đa nhánh (multiple conditions)
        # [8, 10]: Giỏi
        # [6.5, 8): Khá
        # [5, 6.5): TB
        # [0, 5): Yếu


        # INPUT score
        # IF score >= 8 AND score <= 10 THEN
            # OUTPUT 'Xếp loại: Giỏi'
        # ELSE IF score >= 6.5 AND score < 8 THEN
            # OUTPUT "Xếp loại: Khá"
        # ELSE IF score >= 5 AND score < 6.5 THEN
            # OUTPUT "Xếp loại: Trung Bình"
        # ELSE IF score >= 0 AND score < 5 THEN
            # OUTPUT "Xếp loại: Yếu"
        # ELSE
            # OUTPUT "Bạn đã nhập sai điểm"
        # ENDIF

score = float(input('Nhập điểm: '))
if 8 <= score <= 10:        # if (score >= 8) and (score <= 10):
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: TB')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Điểm không hợp lệ')

# ============ LUYỆN TẬP =================
# Bài 1: Nhập 1 số nguyên n từ bàn phím.
    # Nếu n là số chẵn thì in ra "Đây là số chẵn"
    # Nếu n là số lẻ thì in ra "Đây là số lẻ"

    # INPUT n
    # IF n% 2 == 0 THEN
        # OUTPUT 'Đây là số chẵn'
    # ELSE
        # OUTPUT "Đây là số lẻ"
    # ENDIF

n = int(input('Nhập số nguyên n: '))
if n % 2 == 0:
    print('Đây là số chẵn')
else:
    print('Đây là số lẻ')

# Bài 2: Nhập điểm số của bạn từ bàn phím.
# Yêu cầu: Xếp loại học lực học sinh. Biết rằng:
    # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu

    # INPUT score
    # IF score > 10 OR score < 0 THEN
        # OUTPUT "Điểm không hợp lệ"
    # ELSE
        # IF score >= 8 THEN
            # OUTPUT 'Xếp loại: Giỏi'
        # ELSE IF score >= 6.5 THEN
            # OUTPUT "Xếp loại: Khá"
        # ELSE IF score >= 5 THEN
            # OUTPUT "Xếp loại: Trung Bình"
        # ELSE
            # OUTPUT "Xếp loại: Yếu"
        # ENDIF
    # ENDIF

score = float(input('Nhập điểm: '))
if score > 10 or score < 0:
    print('Điểm không hợp lệ')
else:
    if score >= 8:
        print('Xếp loại: Giỏi')
    elif score >= 6.5:
        print('Xếp loại: Khá')
    elif score >= 5:
        print('Xếp loại: TB')
    else:
        print('Xếp loại: Yếu')

# Bài 3: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.