import oop

h1 = oop.Human("Trung", 30, "Male")

print(h1.name)
print(h1.get_age())

h1.speak()

st1 = oop.Student("An", 20, "Male", "S123")
print(st1.name)
# Kế thừa phương thức từ lớp cha
print(st1.get_age())
print(st1.speak())

h1.introduce()
st1.introduce()

# Đề bài:
# Tạo class Animal gồm các thuộc tính: tên, loài
# Viết 2 phương thức cho class Animal

# Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
# Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
# Viết 1 phương thức mới cho class Dog

# Yêu cầu:
# - Tạo class ở file oop.py
# - Viết chương trình test tại file main.py

a1 = oop.Animal("Pororo", "penguin")
a2 = oop.Animal("Loopy", "beaver")
a1.display_info()
a1.eat("fish")

dog1 = oop.Dog("Buddy", "Dog", "Husky")
dog1.display_info()
print(dog1)

# Bài tập 2:
# Hãy xây dựng các lớp cha và lớp con như đã xác định. Lưu ý lớp cha có những đặc điểm sau:
# 	hang: Tên của hãng xe
# 	mau_sac: Màu sắc của xe
# 	gia_tien: GIá tiền của xe.
# Phương thức khoi_dong(): In ra màn hình “Xe {hãng} đang khởi động”

# Lớp con có những phương thức sau khác lớp cha:
# 	Phương thức dap_bang_hai_chan(): In ra màn hình “Xe {hãng} đang được đạp về phía trước”
# 	Phương thức chay_bang_bon_banh(): In ra màn hình “Xe {hãng} đang chạy về phía trước bằng động cơ”
# Hãy chọn phương thức phù hợp với từng lớp và hoàn thiện các lớp con có sử dụng kế thừa.

b1 = oop.Bicycle("Thống nhất", "Xanh", 500)
c1 = oop.Car("Toyota", "Đen", 20000)

b1.start()
c1.start()