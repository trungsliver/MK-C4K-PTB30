# Bài 1: Viết hàm/chương trình con kiểm tra 1 số có phải là số nguyên tố hay không, biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó.
# In ra số nguyên tố trong khoảng [10,100].
def is_prime(n: int):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

for i in range (10,101):
    if is_prime(i) == True:
        print(i, end=' ')

# Bài 2: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
# Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
a = input('Nhập 10 số nguyên cách nhau bởi khoảng trắng: ')
arr1 = a.split()
print('Danh sách vừa nhập:', arr1)

# Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
numList = []
for item in arr1:
    numList.append(int(item))
print(numList)

# Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.
count = 0
for item in numList:
    if item % 2 != 0:
        count += 1
print('Số lượng số lẻ trong danh sách là:', count)

# Yêu cầu 4: Sắp xếp các phần tử trong danh sách num_list theo thứ tự từ lớn đến nhỏ.
numList.sort(reverse=True)
print('Danh sách sau khi sắp xếp:\n', numList)

# Bài 3: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2. 
import random
arr1 = []
arr2 = []
for i in range(10):
    arr1.append(random.randint(20, 50))
    arr2.append(random.randint(20, 50))
print('Danh sách 1:', arr1)
print('Danh sách 2:', arr2)

# Yếu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
def common_elements(arr1, arr2):
    for item in arr1:
        for item2 in arr2:
            if item == item2:
                print(item, end=' ')
common_elements(arr1, arr2)

# Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
for i in range(len(arr1)):
    if arr1[i] == min(arr1):
        print(f'\nVị trí phần tử nhỏ nhất của danh sách arr1 là: {i}')

# Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2
for i in range(len(arr2)):
    if arr2[i] == max(arr2):
        print(f'\mVị trí phần tử lớn nhất của danh sách arr2 là: {i}')

# Bài 4: Hãy nhập từ bàn phím họ tên của bạn.
name = input('Nhập họ tên của bạn: ')
name = 'tOnG mY LInH'
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
name_upper = name.upper()
print(name_upper)
# Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
name_lower = name.lower()
print(name_lower)
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu
name_title = name.title()
print(name_title)
