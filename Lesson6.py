# Vòng lặp vô hạn - Vòng lặp while
# Vòng lặp không biết trước số lần lặp

for i in range(6):
    print(i, end=' ')

    # SET i TO 0
    # WHILE i < 6 DO
    #     OUTPUT i
    #     SET i TO i+1
    # END WHILE

i = 0
while i < 6:
    print(i, end = ' ')
    i = i + 1           # i += 1

# Các lệnh thoát vòng lặp
    # break: thoát khỏi vòng lặp, bỏ qua các lần lặp kế tiếp
    # continue: bỏ qua lần lặp hiện tại, chuyển sang lần lặp kế tiếp

print('\n Ví dụ break:')
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print('\n Ví dụ continue:')
for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')

# Bài 1: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại

    # INPUT n
    # WHILE n < 0 OR n > 100 DO
    #     OUTPUT 'Bạn đã nhập sai, vui lòng nhập lại!
    #     INPUT n
    # END WHILE
    # OUTPUT 'Nhập n thành công!'

n = int(input('\nNhập số nguyên n trong khoảng [0,100]: '))
while n < 0 or n > 100:
    print('Bạn đã nhập sai, vui lòng nhập lại!')
    n = int(input('Nhập số nguyên n trong khoảng [0,100]: '))
print('Nhập n thành công!')

#  Bài 2: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random) trong khoảng [0,100]
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Nếu người chơi đoán sai, có gợi ý (số cần tìm lớn hơn / nhỏ hơn)
    # Đếm sỗ lần người chơi đoán đến khi chiến thắng

    # SET number TO random number between 0 and 20
    # SET count TO 1
    # INPUT guess
    # WHILE guess != number DO
    #     IF guess > number THEN
    #         OUTPUT 'Số cần tìm nhỏ hơn', guess
    #     ELSE
    #         OUTPUT 'Số cần tìm lớn hơn', guess
    #     END IF
    #     SET count TO count + 1
    #     INPUT guess
    # END WHILE
    # OUTPUT 'Bạn đã đoán đúng sau', count, 'lần thử'

import random
number = random.randint(0,100)
count = 1
guess = int(input('\nNhập dự đoán của bạn: '))
while guess != number:
    if guess > number:
        print('Số cần tìm nhỏ hơn', guess)
    else:
        print('Số cần tìm lớn hơn', guess)
    guess = int(input('\nNhập dự đoán của bạn: '))
    count = count + 1
print(f'Bạn đã đoán đúng sau {count} lần thử!')

# Bài 3: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
# Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6

    # INPUT n
    # SET sum TO 0
    # IF n < 0 THEN
    #     OUTPUT 'Bạn đã nhập sai'
    # ELSE
    #     WHILE n > 0 DO
    #         SET sum TO sum + (n%10)
    #         SET n TO n/10
    #     END WHILE
    #     OUTPUT 'Tổng các chữ số là:', sum
    # ENDIF

n = int(input('Nhập số nguyên dương n: '))      # Nhập n
sum = 0                                         # biến sum lưu tổng các chữ số
# print(len(str(n)))
if n < 0:
    print('Bạn đã nhập sai')
else:
    while n > 0:
        sum = sum + (n%10)                      # cộng chữ số hàng đơn vị vào sum
        n = n // 10                             # xóa chữ số hàng đơn vị
    print('Tổng các chữ số là:', sum)

# ================ ÔN TẬP VÒNG LẶP FOR =====================
# Dạng 1: In / Hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = int(input('Nhập n: '))
for i in range(n + 1):
    print(i, end=' ')

    # 1.2. In ra màn hình các số trong khoảng [a,b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else: 
    for i in range(b, a + 1):
        print(i, end=' ')

    # 1.3. In ra các số chẵn trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end = ' ')

    # 1.4. In ra các số lẻ trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
for i in range(a, b+1):
    if i % 2 != 0:
        print(i, end = ' ')

# Dạng 2: Tính tổng
    # 2.1. Tính tổng các số trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
sum = 0
for i in range(a, b+1):
    sum += i    # sum = sum + i
print(f'Tổng các số trong khoảng [{a},{b}] là: {sum}')

    # 2.2. Tính tổng các số chẵn trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum += i    # sum = sum + i
print(f'Tổng các số chẵn trong khoảng [{a},{b}] là: {sum}')

        # 2.2. Tính tổng các số dương trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
sum = 0
for i in range(a, b+1):
    if i > 0:
        sum += i    # sum = sum + i
print(f'Tổng các số dương trong khoảng [{a},{b}] là: {sum}')

# Dạng 3: Đếm số lượng
    # 3.1. Đếm số lượng các số trong khoảng [a.b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
count = 0
for i in range(a, b+1):
        count += 1
print(f'Số lượng số trong khoảng [{a},{b}] là: {count}')

    # 3.2. Đếm số lượng số lẻ trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
count = 0
for i in range(a, b+1):
        if i % 2 != 0:
            count += 1
print(f'Số lượng số lẻ trong khoảng [{a},{b}] là: {count}')

    # 3.3. Đếm số lượng số chia hết cho 5 trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
count = 0
for i in range(a, b+1):
        if i % 5 == 0:
            count += 1
print(f'Số lượng số chia hết cho 5 trong khoảng [{a},{b}] là: {count}')