# tuple trong python

# giới tính
gioiTinh = ("Nam", "Nữ")
# lớp học phổ thông
lopHoc = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# in ra giới tính ở vị trí 0
print ("Giới tính: ", gioiTinh[0])
# lopHoc[0] = 13 # không thể thay đổi giá trị
# duyệt qua từng phần tử bằng for/ while
for lop in lopHoc:
    print ("Lớp: ",lop)
# cộng 2 tuple
x = (1,2,3)
y = (4,5,6)
z = x + y
print ("z=",z)
# nhân 2 tuple
x = x*2
print ("x=",x)
# kiểm tra phần tử tồn tại trong tuple
if 12 in lopHoc:
    print ("Tồn tại")
else:
    print ("Không tồn tại")
# lấy độ dài tuple
print ("độ dài của lớp học:",len (lopHoc))
# số lần xuất hiện của số 1 trong x
print ("{0} lần".format (x.count(1)))
# min max sum
print ("Giá trị nhỏ nhất:",min (lopHoc))
print ("Giá trị lớn nhất:",max (lopHoc))
print ("Giá trị tổng:",sum (lopHoc))
# sắp xếp tuple
listX = sorted (x)
print (listX)
print (type (listX))