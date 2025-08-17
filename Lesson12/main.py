import oop

# Khởi tạo đối tượng cụ thể
h1 = oop.Human("Duc Trung", 27, "male")
h2 = oop.Human("My Linh", 13, "female")

# Sử dụng phương thức introduce()
h1.introduce()
h2.introduce()

# Sử dụng phương thức __str__
print(h1)

# Sử dụng phương thức display_info()
h1.display_info()
h2.display_info()

# Sử dụng phương thức hát
h1.sing("Shape of You")
h2.sing("Let It Go")

# Bài tập thứ cưng
a1 = oop.ThuCung("Tom", "Mèo", "blue", 2, 3.5)
a1.display_info()
a1.change_color("white")
# a1.change_color2()

# Bài tập bank account
acc1 = oop.BankAccount("ductrung", 1000)
acc1.display_info()
acc1.deposit()
acc1.withdraw()
acc1.deposit2(80)
acc1.withdraw2(125.5)