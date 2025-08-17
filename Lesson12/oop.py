# Lập trình hướng đối tương
# OOP - Object Oriented Programming

# Tổng quát: OOP là cách mà chúng ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Ví dụ: mô phỏng Human
    # Attributes (thuộc tính): đặc điểm (tên, tuổi, giới tính,....)
    # Methods (phương thức): hành động (nói, đi, ăn,....)

# Khai báo lớp đối tượng
class Human:
    # Hàm khởi tạo giá trị (hàm có sẵn)
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức
    # Phương thức giới thiệu
    def introduce(self):
        print(f'Xin chào, tôi là {self.name}')

    # Phương thức hiển thị thông tin (có sẵn, dùng được print)
    def __str__(self):
        return f'Tên: {self.name}, Tuổi: {self.age}, Giới tính: {self.gender}'

    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'''
==============Thông tin==============
Tên:        {self.name}
Tuổi:       {self.age}
Giới tính:  {self.gender}
=====================================''')
        
    # Phương thức hát
    def sing(self, song):
        print(f'{self.name} đang hát bài {song}')
        
class ThuCung:
    def __init__(self, name, species, color, age, weight):
        self.name = name
        self.species = species
        self.color = color
        self.age = age
        self.weight = weight

    def display_info(self):
        print(f'''
==============Thông tin==============
Tên:        {self.name}
Loài:       {self.species}
Màu sắc:    {self.color}
Tuổi:       {self.age}
Cân nặng:   {self.weight}
=====================================''')
        
    # Cách 1    
    def change_color(self, new_color):
        self.color = new_color
        print(f'Màu sắc của {self.name} đã được thay đổi thành {self.color}')
        # Hiển thị lại thông tin sau thay đổi
        self.display_info()

    # Cách 2
    def change_color2(self):
        new_color = input(f'Nhập màu sắc mới cho {self.name}: ')
        self.color = new_color
        print(f'Màu sắc của {self.name} đã được thay đổi thành {self.color}')
        # Hiển thị lại thông tin sau thay đổi
        self.display_info()

class BankAccount:
    # Hàm khởi tại
    def __init__(self, acc_number, balance:float):
        # Số tài khoản / tên tài khoản
        self.acc_number = acc_number
        # Số dư tài khoản
        self.balance = balance

    def display_info(self):
        print(f'''
==============Thông tin tài khoản==============
Số tài khoản:   {self.acc_number}
Số dư:          ${self.balance}
=====================================''')
        
    # Phương thức nạp tiền
    def deposit(self):
        amount = float(input('Nhập số tiền cần nạp: $'))
        if amount > 0:
            # tăng số dư
            self.balance += amount
            print(f'Đã nạp ${amount} vào tài khoản.')
        else:
            print('Số tiền nạp không hợp lệ.')
        # Hiển thị lại thông tin tài khoản
        self.display_info()

    # Phương thức rút tiền
    def withdraw(self):
        amount = float(input('Nhập số tiền cần rút: $'))
        if 0 < amount <= self.balance:
            # giảm số dư
            self.balance -= amount
            print(f'Đã rút ${amount} khỏi tài khoản.')
        else:
            print('Số tiền rút không hợp lệ.')
        # Hiển thị lại thông tin tài khoản
        self.display_info()

    # Phương thức nạp tiền
    def deposit2(self, amount:float):
        if amount > 0:
            # tăng số dư
            self.balance += amount
            print(f'Đã nạp ${amount} vào tài khoản.')
        else:
            print('Số tiền nạp không hợp lệ.')
        # Hiển thị lại thông tin tài khoản
        self.display_info()

    # Phương thức rút tiền
    def withdraw2(self, amount:float):
        if 0 < amount <= self.balance:
            # giảm số dư
            self.balance -= amount
            print(f'Đã rút ${amount} khỏi tài khoản.')
        else:
            print('Số tiền rút không hợp lệ.')
        # Hiển thị lại thông tin tài khoản
        self.display_info()