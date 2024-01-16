# cấu trúc rẽ nhánh

x = int (input ("Nhập x: "))
kq = "Chẵn" if (x %2 == 0) else "Lẻ" # đây gọi là toán tử 3 ngôi
print (x, "là số",kq)
if x > 0:
    print (x,"là số dương")
else:
    print (x,"là số âm")
diemThi = float (input("Nhập vào điểm thi cuối kì: "))
if diemThi >= 8:
    print ("Học sinh giỏi")
elif diemThi >= 6.5:
    print ("Học sinh khá")
elif diemThi >= 5:
    print ("Học sinh trung bình")
else:
    print ("Học sinh yếu")
