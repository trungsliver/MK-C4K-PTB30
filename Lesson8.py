# Strings - Chuỗi / xâu ký tự
name = "Duc Trung"

# Độ dài string - len()
print("len:", len(name))

# Truy cập từng ký tự trong string
    # Truy cập bằng index
print('Ký tự đầu tiên:', name[0])
print('Ký tự cuối cùng:', name[-1])

    # Duyệt string
        # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'Ký tự thứ {i+1}: {name[i]}')

        # Cách 2: Chỉ dùng value
for char in name:
    print(f'Ký tự: {char}')

# Xâu con
str1 = "Tong My Linh"
str2 = "My Linh"
str3 =  "dep trai"

    # Kiểm tra xâu con: in
print('str2 có nằm trong str1 không:', str2 in str1)    # Output: True
print('str3 có nằm trong str1 không:', str3 in str1)    # Output: False

    # Tìm vị trí xâu con: find() => index
print(str1.find('Linh'))        # Output: 8
print(str1.find(str2))          # Output: 5
print(str1.find(str3))          # Output: -1

# Slicing - cắt chuỗi
name = 'hahahihihuhu'
for i in range(len(name)):
    print(f'{i}: {name[i]}')
    # cắt ở vị trí bất kì
print(name[4:8])                # Output: hihi
    # cắt từ đầu string
print(name[:4])                 # Output: haha
    # cắt đến cuối string
print(name[8:])                 # Output: huhu

# Tách chuỗi - split()
    # Mặc định tách khi gặp khoảng trắng
a = '1 2 3 4 5 6 7 8 9'
arr1 = a.split()
print(arr1)
    # Tùy chỉnh
b = 'a,b,c,d,e,g,h,i,k'
arr2 = b.split(',')
print(arr2)

# Xóa khoảng trắng ở đầu và cuối chuỗi
name1 = '    Tong My Linh     '
print(name1)
print(name1.strip())

# Thay thế string - replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song2 = song.replace('doo', 'linh')
# song4 = song2.replace('linh', 'doo', 3)
print(song2)
    # Thay thế với số lượng nhất định
song3 = song.replace('doo', 'linh', 3)
print(song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
str1 = ' '.join(arr)
str2 = ''.join(arr)
str3 = '_'.join(arr)
print(str1)
print(str2)
print(str3)

# Viết hoa - viết thường
name = 'Tran Van thanh'
    # Viết hoa tất cả - upper()
print(name.upper())
    # Viết thường tất cả - lower()
print(name.lower())
    # Viết hoa chữ cái đầu mỗi từ - title()
print(name.title())
    # đồi thường => hoa và ngược lại
print(name.swapcase())

    # Ví dụ thực tế
# tên gốc: x = 'mindX'
# Người dùng: y = 'Mindx'
# so sánh: x.lower() == y.lower()
x = 'mindX Technology School'
y = 'Mindx'
print(x == y)
print(y.lower() in x.lower())

# Chuyển đổi kiểu dữ liệu trong danh sách
a = '1 2 3 4 5 6 7 8 9'
strList = a.split()    # Dạng string
print(strList)
    # Cách 1:
numList = []            # Khai báo danh sách rỗng
for item in strList:
    new_value = int(item)
    numList.append(new_value)
print(numList)
    # Cách 2:
numList2 = [int(item) for item in strList]
print(numList2)

# Tính tổng phần tử danh sách
    # Cách cũ:
sumAll = 0
for item in numList:
    sumAll += item
print('Tổng các phần tử danh sách:', sumAll)
    # cách mới:
sumAll2 = sum(item for item in numList)
print('Tổng các phần tử danh sách:', sumAll2)

# Tính tổng các phần tử chẵn của danh sách
    # cách cũ:
sumEven = 0
for item in numList:
    if item % 2 == 0:
        sumEven += item
print('Tổng các phần tử chẵn:', sumEven)
    # cách mới:
sumEven2 = sum(item for item in numList if item%2==0)
print('Tổng các phần tử chẵn:', sumEven2)

# Đếm số lượng số lẻ trong danh sách
    # cách cũ
countOdd = 0
for item in numList:
    if item % 2 != 0:
        countOdd += 1
print('Số lượng phần tử lẻ:', countOdd)
    # cách mới
countOdd2 = sum(1 for item in numList if item%2!=0)
print('Số lượng phần tử lẻ:', countOdd2)

# ================= LUYỆN TẬP =========================
# Bài 1: Nhập 2 thông tin: họ, tên và lưu vào 2 biến khác nhau
# In ra màn hình tên đầy đủ và viết hoa chữ cái đầu mỗi từ
lastName = input('Nhập họ của bạn: ')
firstName = input('Nhập tên của bạn: ')
arr = [lastName.strip(), firstName.strip()]
fullName = ' '.join(arr)
print('Tên đầy đủ:', fullName.title())

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
date1 = input('Nhập chuỗi dạng dd/mm/yyyy: ')

    # Cách 1: split()
x = date1.split('/')
day = x[0]
month = x[1]
year = x[2]
print("Ngày:", day, '\nTháng:', month, '\nNăm:', year)

    # Cách 2: dùng replace()
date2 = date1.replace('/', ' tháng ', 1)
date3 = date2.replace('/', ' năm ', 1)
print(date3)

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc

    # Khai báo thông tin đúng
correct_username = "ductrung"
correct_password = "123456"

    # Kiểm tra thông tin người dùng nhập vào
while True:
    # Người dùng nhập thông tin
    data = input('Nhập thông tin dạng "username:password": ')

    #  Kiểm tra data có chứa ":" không
    if ':' not in data:
        print('Sai định dạng. Vui lòng nhập lại!')
        continue

    # tách username và password
    username, password = data.split(":", 1)

    # Kiểm tra với thông tin đúng
    if username == correct_username and password == correct_password:
        print('Đăng nhập thành công!')
        break
    else:
        print('Sai thông tin. Vui lòng nhập lại!')

