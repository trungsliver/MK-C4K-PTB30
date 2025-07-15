# Bài 3: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.

# hs1 = float(input('Nhập điểm hs1: '))
# hs2 = float(input('Nhập điểm hs2: '))
# hs3 = float(input('Nhập điểm hs3: '))

# # Tìm bạn có điểm thấp nhất
# if hs1 == hs2 == hs3:  
#     print('3 bạn học sinh có điểm bằng nhau')
# elif hs1 == hs2 and hs1 < hs3:
#     print('Học sinh 1 và 2 có điểm thấp nhất')
# elif hs1 == hs3 and hs1 < hs2:
#     print('Học sinh 1 và 3 có điểm thấp nhất')
# elif hs2 == hs3 and hs2 < hs1:
#     print('Học sinh 2 và 3 có điểm thấp nhất')
# elif hs1 < hs2 and hs1 < hs3:
#     print('Học sinh 1 có điểm thấp nhất')
# elif hs2 < hs1 and hs2 < hs3:
#     print('Học sinh 2 có điểm thấp nhất')
# elif hs3 < hs1 and hs3 < hs2:
#     print('Học sinh 3 có điểm thấp nhất')
# else:
#     print('Lỗi')

# Câu 1: Nhập một số từ bàn phím và in ra số đó.
num = int(input('Nhập 1 số bạn  thích: '))
print('Số bạn vừa nhập là:', num)

# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
    # INPUT num
    # IF num % 2 == 0 THEN
    #     PRINT 'Số bạn vừa nhập là số chẵn'
    # ELSE
    #     PRINT 'Số bạn vừa nhập là số lẻ'
    # ENDIF

num = int(input('Nhập 1 số nguyên: '))
if num % 2 == 0:
    print('Số bạn vừa nhập là số chẵn')
else:
    print('Số bạn vừa nhập là số lẻ')


# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương của hai số nhập từ bàn phím.
    # INPUT a
    # INPUT b
    # OUTPUT 'Tổng của a và b là:'          + (a + b)
    # OUTPUT 'Hiệu của a và b là:'          + (a - b)
    # OUTPUT 'Tích của a và b là:'          + (a * b)
    # OUTPUT 'Trung bình của a và b là:'    + (a / b)

a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
print('Tổng 2 số là:', a+b)
print('Hiệu 2 số là:', a-b)
print('Tích 2 số là:', a*b)
print('Thương 2 số là:', a/b)

# Câu 4: Viết chương trình nhập vào 1 số nguyên và in ra màn hình giá trị tuyệt đối của số đó.
    # INPUT num
    # IF num >= 0 THEN
    #     OUTPUT 'Giá trị tuyệt đối của số bạn vừa nhập là:' + num
    # ELSE
    #     OUTPUT 'Giá trị tuyệt đối của số bạn vừa nhập là:' + (-num)
    # ENDIF

num = int(input('Nhập 1 số nguyên: '))
if num >= 0:
    print('Giá trị tuyệt đối của số bạn vừa nhập là:', num)
else:
    print('Giá trị tuyệt đối của số bạn vừa nhập là:', -num)

# Câu 5: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
    # INPUT usd
    # SET vnd TO usd * 26000
    # OUTPUT "Số tiền VND là: " + vnd

usd = float(input('Nhập số USD muốn đổi: $'))
vnd = usd * 26000
print("Số tiền VND là: " + str(vnd))
print(f'${usd} = {vnd} VND')

# Câu 6: Viết chương trình nhập vào một số nguyên time là số giây cần xử lý. 
# Hãy đối số giây cho trước thành số giờ, phút, giây và in kết quả ra màn hình.
# VD: 3662s = 1h 1p 2s
# Gợi ý:
    # 1h = 3600s, 1p = 60s

time = int(input('Nhập số giây cần xử lý: '))

h = time // 3600
m = (time % 3600) // 60
s = time % 60

print(f'{time}s = {h}h {m}m {s}s')

# Tính tiền điện
    # Nhập số kW đã sử dụng:
    # Quy tắc tính tiền điện:
        # Giá điện kW 0-100: 1500đ/kW
        # Giá điện kW 101-200: 2000đ/kw
        # Giá điện kw lớn hơn 200: 4000đ/kw
    # VD: sử dụng 50kw => tiền điện = 50 * 1500
    #       sử dụng 500kW => tiền điện = 100*1500 + 100*2000 + 300*4000

kw = float(input('Nhập số kW điện đã sử dụng: '))
cash = 0

if kw < 0:
    print('Bạn đã nhập sai dữ liệu.')
elif kw >= 0 and kw <= 100:
    cash = kw * 1500
elif kw > 100 and kw <= 200:
    cash = 100 * 1500 + (kw-100) * 2000
else:
    cash = 100 * 1500 + 100 * 2000 + (kw-200) * 4000

print('Số tiền cần trả là:', cash)