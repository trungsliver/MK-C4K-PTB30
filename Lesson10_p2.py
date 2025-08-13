# Ôn tập:
# Bài 1: Nhập vào từ bàn phím các thông tin các nhân: 
    # Họ tên, Tuổi, Trường học, giới tính, điểm trung bình.
    # In ra màn hình các thông tin vừa nhập
name = input('Nhập tên: ')
age = int(input('Nhập tuổi: '))
school = input('Nhập trường học: ')
gender = input('Nhập giới tính: ')
score = float(input('Nhập điểm trung bình: '))
print(f'''
Họ tên: {name}
Tuổi: {age}
Trường học: {school}
Giới tính: {gender}
Điểm: {score}''')

# Bài 2: Nhập vào chiều dài và chiều rộng hình chữ nhật
    # In ra màn hình chu vi và diện tích hình chữ nhật đó.
a = float(input('Nhập chiều dài: '))
b = float(input('Nhập chiều rộng: '))
chuvi = 2 * (a + b)
dtich = a * b
print(f'Chu vi HCN:', chuvi)
print(f'Diện tích HCN:', dtich)

# Bài 3: Nhập số nguyên n từ bàn phím.
    # Kiểm tra xem n có phải là số chẵn hay không.
n = int(input('Nhập số nguyên n: '))
if n % 2 == 0:
    print(f'{n} là số chẵn')
else:
    print(f'{n} là số lẻ')

# Bài 4: Nhập điểm số từ bàn phím. Hãy in ra mà hình xếp hạng học lực, biết rằng:
    # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
score = float(input('Hãy nhập điểm của bạn: '))
if 8 <= score <= 10:
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: Trung bình')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Điểm không hợp lệ')

# Bài 5: Nhập 2 số nguyên a và b từ bàn phím
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
if b >= a:
    print(f'Các số trong khoảng [{a}, {b}] là:')
    for i in range(a, b + 1):
        print(i, end = ' ')
else:
    print(f'Các số trong khoảng [{b}, {a}] là:')
    for i in range(b, a + 1):
        print(i, end = ' ')

    # Yêu cầu 2: Tính tổng các số chia hết cho 3 trog khoảng vừa in
sum = 0
if b >= a:
    for i in range(a, b + 1):       # Duyệt vòng lặp chạy từ a đến b
        if i % 3 == 0:              # Kiểm tra i chia hết cho 3
            sum += i                # Cộng i vào biến sum
    print(f'Tổng các số chia hết cho 3 trong khoảng [{a}, {b}] là:', sum)
else:
    for i in range(b, a + 1):       # Duyệt vòng lặp chạy từ b đến a
        if i % 3 == 0:              # Kiểm tra i chia hết cho 3
            sum += i                # Cộng i vào biến sum
    print(f'Tổng các số chia hết cho 3 trong khoảng [{b}, {a}] là:', sum)
            
    # Yêu cầu 3: In ra số lượng số lẻ có trong khoảng trên
count = 0
if b >= a:
    for i in range(a, b + 1):       # Duyệt vòng lặp chạy từ a đến b
        if i % 2 != 0:              # Kiểm tra số lẻ
            count += 1              # Tăng count thêm 1
    print(f'Số lượng số lẻ trong khoảng [{a}, {b}] là:', count)
else:
    for i in range(b, a + 1):       # Duyệt vòng lặp chạy từ b đến a
        if i % 2 != 0:              # Kiểm tra số lẻ
            count += 1              # Tăng count thêm 1
    print(f'Số lượng số lẻ trong khoảng [{b}, {a}] là:', count)

    # Yêu cầu 4: Tính trung bình cộng các số trong khoảng trên (làm tròn đến chữ số thập phân thứ 2)
sum = 0
count = 0
if b >= a:
    for i in range(a, b + 1):       # Duyệt vòng lặp chạy từ a đến b
        sum += i                    # Cộng i vào biến sum
        count += 1                  # Tăng count thêm 1
    tbc = round(sum/count, 2)
    print(f'Trung bình cộng các số trong khoảng [{a}, {b}] là:', tbc)
else:
    for i in range(b, a + 1):       # Duyệt vòng lặp chạy từ b đến a
        sum += i                    # Cộng i vào biến sum
        count += 1                  # Tăng count thêm 1
    tbc = round(sum/count, 2)
    print(f'Trung bình cộng các số trong khoảng [{b}, {a}] là:', tbc)

# Bài 6: In ra bảng cửu chương từ 5 đến 9
for i in range(5, 10):
    print('\nBảng cửu chương', i)
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')

# Bài 7: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
    # Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6
n = int(input('Nhập số nguyên dương n: '))   
sum = 0
while n > 0:              # Duyệt số n cho đến khi n = 0
    sum = sum + n%10      # Lấy hàng đơn vị của n
    n = n // 10           # Loại bỏ hàng đơn vị của n
print('Tổng các chữ số:', sum)

# Bài 8: Nhập n là số giây cần chuyển đổi (số nguyên)
    # In ra màn hình dạng h-m-s
    # Ví dụ: 3661s = 1h 1p 1s
# Nhập số giây từ bàn phím
seconds = int(input("Nhập số giây cần chuyển đổi: "))
# Chuyển đổi số giây sang giờ, phút, giây
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# # Bài 9: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
a = input('Nhập 10 số nguyên cách nhau bởi khoảng trắng: ')
arr1 = a.split()
print('Danh sách vừa nhập:', arr1)
        # Chuyển các phần tử từ str => int
numList = []
for item in arr1:
    numList.append(int(item))
print(numList)

    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
numList.insert(2, -5)
print(numList)

    # YC3: Tính tổng các cố chẵn trong danh sách
sum_even = 0
for item in numList:                # Cách duyệt số 2: chỉ dùng value
    if item % 2 == 0:           # Kiểm tra số chẵn
        sum_even += item        # cộng phần tử chẵn vào biến tổng
print('Tổng các số chẵn:', sum_even)

    # YC4: Đếm số lượng số lẻ có trong danh sách
count_odd = 0
for item in numList:                # Cách duyệt số 2: chỉ dùng value
    if item % 2 != 0:           # Kiểm tra số lẻ
        count_odd += 1          # tăng count thêm 1
print('Số lượng số lẻ:', count_odd)
    
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
max_value = max(numList)
print('Giá trị lớn nhất trong danh sách:', max_value)

    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
for i in range(len(numList)):
    if numList[i] == min(numList):
        print('Vị trí phần tử nhỏ nhất:', i)

    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách
def avg_list(arr):
    if len(arr) == 0:
        return 'Danh sách rỗng!'
    else:
        sum = 0
        for item in arr:
            sum += item
        return round(sum/len(arr), 2)
print('Giá trị trung bình của các phần tử trong danh sách:', avg_list(numList))