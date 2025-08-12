# Hàm - chương trình con
    # hàm không có giá trị trả về
def say_hello():
    print("Hello Linh")
    print("hello Trung")
# say_hello()

    # Hàm có tham số truyền vào
def say_hello_to(name):
    print("Hello", name)
# say_hello_to("Linh")
# say_hello_to("Trung")

    # Hàm có giá trị trả về
def dtich_HCN(a:float, b:float):
    return a * b
# print("Diện tích hình chữ nhật là:", dtich_HCN(5, 10))

# ví dụ:
def cvi_tam_giac(a:float, b:float, c:float):
    return a+b+c

# canh1 = float(input("Nhập cạnh 1: "))
# canh2 = float(input("Nhập cạnh 2: "))   
# canh3 = float(input("Nhập cạnh 3: "))
# print("Chu vi tam giác là:", cvi_tam_giac(canh1, canh2, canh3))

# =================== LUYỆN TẬP ===================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
numbers = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]
def sum_odd(arr):
    sum = 0                 # Khai báo biến lưu tổng
    for item in arr:        # Duyệt danh sách, cách 2 - chỉ có giá trị
        if item % 2 != 0:   # Kiểm tra số lẻ
            sum += item     # Cộng giá trị phần tử vào biến sum
    return sum              # Trả về giá trị sum khi duyệt xong vòng lặp
print('Tổng số lẻ trong danh sách:', sum_odd(numbers))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n:int):
    count = 0                   # Khai báo biến đếm 
    for i in range(1, n + 1):   # Duyệt số từ 1 đến n
        if n % i == 0:          # Kiểm tra n có chia hết cho i không
            count += 1          # Chia hết thì tăng count thêm 1
    if count == 2:              # count = 2 thì n là số nguyên tố
        return True             # Trả về True
    else:                       # count != 2 thì n không phải số nguyên tố
        return False            # Trả về False

print('7:', is_prime(7))  # True
print('8:',is_prime(8))  # False
  

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
str1 = 'Tống Mỹ Linh mặc áo màu ghi'
def count_words(s):
    # strip(): Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    # split(): Tách chuỗi thành danh sách các từ dựa trên khoảng trắng
    arr = s.strip().split()  
    return len(arr)  # Trả về số lượng từ trong danh sách
print('Số lượng từ trong chuỗi:', count_words(str1))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    while n <= 0:                # Duyệt khi n > 0
        print("Vui lòng nhập số nguyên dương")
        n = int(input("\nNhập lại số nguyên dương: "))
    sum = 0
    while n > 0:              # Duyệt số n cho đến khi n = 0
        sum = sum + n%10      # Lấy hàng đơn vị của n
        n = n // 10           # Loại bỏ hàng đơn vị của n
    return sum
print('Tổng các chữ số của 12345:', sum_of_digits(12345))  # 15

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
numbers = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]
def find_max(arr):
    max_value = max(arr)        # Tìm giá trị lớn nhất của danh sách
    for i in range(len(arr)):   # Duyệt danh sách, cách 1 - có index
        if arr[i] == max_value: # Tìm vị trí của max_value
            return i            # Trả về vị trí
print('Vị trí phần tử lớn nhất:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n:int):
    sum = 0
    for i in range(1, n+1):  # Duyệt số từ 1 đến n
        sum = sum + i        # Tính tổng các số từ 1 đến n
    return sum
print('Tổng các số từ 1 đến 10:', sum_to_n(10))

