# Comment - ghi chú: Ctrl /

# Khai báo biến - declare variables
    # Lưu trữ dữ liệu
    # Có thể thay đổi được giá trị trong khi lập trình
    # SET <variable> TO <value>
# Python                        # PseudoCode
name = 'Duc Trung'          # SET name TO 'Duc Trung'   
age = 27                    # SET age TO 27
a, b, c = 3, 4, 5

# Nhập dữ liệu - Input
    # INPUT <variable>
# name = input('Hãy nhập tên của bạn: ')      # INPUT name
# age = input('Hãy nhập tuổi của bạn: ')      # INPUT age

# Hiển thị dữ liệu
print(name)                         # OUTPUT name
print('Họ tên: ' + name)            # OUTPUT 'Họ tên ' + name

# Các cách hiển thị ra màn hình
    # Cách 1: Dùng dấu +
print('Họ tên: ' + name) 
# print('Tuổi: ' + age)         # Lỗi 

    # Cách 2: Dùng dấu ,
print('Name:', name)
print('Age:', age)

    # Cách 3: Dùng format - truyền value vào string
print('Tôi tên là ' + name + ', hiện đang ' + str(age) + ' tuổi')
print('Tôi tên là', name, 'hiện đang', age, 'tuổi')
print(f'Tôi tên là {name}, hiện đang {age} tuổi')

    # Cách 4: Hiển thị trên nhiều dòng (trích dẫn)
print(f'''=========================
Bùi Đức Trung
        MindX Technology School
{name} {age}
=============================''')


# Kiểu dữ liệu - Data Types
    # String (str): chuỗi ký tự / xâu ký tự
name = 'Duc Trung'              # SET name TO 'Duc Trung'
    # Interger (int): số nguyên
age = 27                        # SET age TO 27
    # Float (float): số thực, số thập phân
pi = 3.14                       # SET pi TO 3.14
    # Boolean (bool): logic, chỉ có 2 giá trị True/False - Đúng/Sai
male = True                     # set male TO True
female = False                  # set female TO False

# Kiểm tra kiểu dữ liệu - type()
print('Kiểu dữ liệu của name:', type(name))
print('Kiểu dữ liệu của age:', type(age))
print('Kiểu dữ liệu của pi:', type(pi))
print('Kiểu dữ liệu của male:', type(male))

# Xác định kiểu dữ liệu khi nhập (ép kiểu)
teacher = input('Nhập tên giáo viên: ')             # str
yob = int(input('Nhập năm sinh: '))                 # int
height = float(input('Nhập chiều cao: '))           # float
pizza = bool(input('Bạn có thích pizza không: '))   # bool

# =================== LUYỆN TẬP ===================
# Bài 1: Chuyển đổi USD sang VND
    # Bước 1: Nhập dữ liệu usd
    # Bước 2: Chuyển đổi usd sang vnd:  vnd = usd * 26000
    # Bước 3: Hiển thị kết quả

    # INPUT usd
    # SET vnd TO usd * 26000
    # OUTPUT "Số tiền VND là: " + vnd

usd = float(input('Nhập số USD muốn đổi: $'))
vnd = usd * 26000
print("Số tiền VND là: " + str(vnd))
print(f'${usd} = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng HCN.
# Tính chu vi, diện tích HCN và hiển thị ra màn hình
    # Bước 1: Nhập chiều dài, chiều rộng HCN
    # Bước 2: Tính chu vi, diện tích HCN
    # Bước 3: Hiển thị kết quả

    # INPUT cd
    # INPUT cr
    # SET cvi TO (cd + cr) * 2
    # SET dtich TO cd * cr
    # OUTPUT 'Chu vi HCN: ' + cvi
    # OUTPUT 'Diện tích HCN: ' + dtich

cd = float(input('Nhập chiều dài HCN: '))
cr = float(input('Nhập chiều rộng HCN: '))
cvi = (cd + cr) * 2
dtich = cd * cr
print('Chu vi HCN:', cvi)
print('Diện tích HCN:', dtich)
