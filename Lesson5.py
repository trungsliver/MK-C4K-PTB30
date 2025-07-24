# Vòng lặp hữu hạn - Vòng lặp for
# Vòng lặp biết trước số lần lặp

# Cú pháp đầy đủ: range(start, end, step)
    # start: số bắt đầu, mặc định = 0
    # end: số kết thúc (bắt buộc)
    # step: bước nhảy, mặc định = 1
# Lưu ý: chạy từ start => (end-1)

# TH1: range(start, end, step)
for i in range(1, 11, 2):           # FOR i FROM 1 TO 10 STEP 2 DO
    print('Mỹ Linh')                #       OUTPUT 'Mỹ Linh'    
    print(i)                        #       OUTPUT i
                                    # ENDFOR

# TH2: range(start, end)
for i in range(1, 11):
    print(i, end = ' ')

# TH3: range(end)
for i in range(10):
    print(i, end = ' ')

    # Ví dụ:
# range(5,10): 5 => 9
# range(2, 10, 2): 2,4,6,8
# range(-5): không chạy
# range(-10, -5): -10 => -6
# range(1): 0
# range(2,8,3): 2,5
# range(2): 0,1
# range(-5, 2): -5 => 1

# ========== LUYỆN TẬP ===========
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]

    # INPUT a
    # INPUT b
    # FOR i FROM a TO b DO
    #   OUTPUT i
    # ENDFOR

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
print(f'Các số trong khoảng [{a}, {b}] là:')
for i in range (a, b+1):
    print(i, end = ' ')

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b

    # INPUT a
    # INPUT b
    # IF a <= b:
    #   FOR i FROM a TO b DO
    #       OUTPUT i
    #   ENDFOR
    # ELSE
    #   FOR i FROM b TO a DO
    #       OUTPUT i
    #   ENDFOR
    # ENDIF

a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
if a <= b:
    print(f'Các số trong khoảng [{a}, {b}] là:')
    for i in range (a, b+1):
        print(i, end = ' ')
else:
    print(f'Các số trong khoảng [{b}, {a}] là:')
    for i in range (b, a+1):
        print(i, end = ' ')

# Bài 3: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a

    # INPUT a
    # IF 1 <= a <= 10:
    #   FOR i FROM 1 TO 10 DO
    #       OUTPUT a + 'x' + i + '=' + (a*i)
    #   ENDFOR
    # ELSE
    #   OUTPUT 'Không hợp lệ'
    # ENDIF

a = int(input("\nNhập số trong khoảng [1, 10]: "))
if 1 <= a <= 10:
    print(f'Bảng cửu chương của {a} là:')
    for i in range (1, 11):
        print(f'{a} x {i} = {a*i}')
else:
    print('Không hợp lệ')

# Bài 4: In ra màn hình bảng cửu chương từ 2 => 9

    # FOR a FROM 2 TO 9 DO
    #   OUTPUT 'Bảng cửu chương' + a
    #   FOR i FROM 1 TO 10 DO
    #       OUTPUT a + 'x' + i + '=' + (a*i)
    #   ENDFOR
    # ENDFOR

for a in range(2, 10):
    print(f'\nBảng cửu chương của {a} là:')
    for i in range (1, 11):
        print(f'{a} x {i} = {a*i}')
    
# Sử dụng random - ngẫu nhiên
    # Khai báo thư viện
import random
    # Cú pháp sử dụng: [Tên thư viện].[Tên hàm]
# rd = random.randint(1, 10)
# print(rd)

rd1 = random.randint(2, 9)
rd2 = random.randint(2, 9)

print(rd1, rd2)

if rd1 <= rd2:
    for a in range(rd1, rd2+1):
        print(f'\nBảng cửu chương của {a} là:')
        for i in range (1, 11):
            print(f'{a} x {i} = {a*i}')
else:
    for a in range(rd2, rd1+1):
        print(f'\nBảng cửu chương của {a} là:')
        for i in range (1, 11):
            print(f'{a} x {i} = {a*i}')