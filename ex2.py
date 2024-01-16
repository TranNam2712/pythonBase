# khai báo biến và gán giá trị

# gán 1 giá trị cho 1 biến
a = 5
print ("số a =",a)
# gán nhiều giá trị cho nhiều biến
x,y,z = 1,2,"Trần Nhật Nam"
print (x,y,z,sep = ", ")
# gán 1 giá trị cho nhiều biến
x = y = z = "Trần Nhật Nam"
# hằng số: ví dụ với thư viện math với hằng số là pi
import math
print (math.pi); print ()

# kiểu dữ liệu cơ bản (tài liệu)

# ép kiểu dữ liệu

# ép kiểu ngầm định:
a = 10
b = 2.0
c = a / b
print ("Số a=",a)
print ("Số b=",b)
print ("Số c=",c)
print ("Kiểu dữ liệu của a =",type (a))
print ("Kiểu dữ liệu của b =",type (b))
print ("Kiểu dữ liệu của c =",type (c))
# đoạn code sau lỗi gì và cách sửa?
n = 100
m = "200"
# print (m + n) # lỗi vì không thể cộng int và str
# cách sửa
print (n + int(m))
print (str(n) + m); print ()

# các phép toán số học

a = int (input ("Nhập số a:"))
b = int (input ("Nhập số b:"))
# cộng
print ("{0} + {1} = {2}".format (a,b,a + b))
# trừ
print ("{0} - {1} = {2}".format (a,b,a - b))
# nhân
print ("{0} * {1} = {2}".format (a,b,a * b))
# chia
print ("{0} / {1} = {2}".format (a,b,a / b))
# chia lấy dư
print ("{0} % {1} = {2}".format (a,b,a % b))
# mũ
print ("{0} ** {1} = {2}".format (a,b,a ** b))
# chia lấy phần nguyên
print ("{0} // {1} = {2}".format (a,b,a // b)); print ()

# toán tử so sánh và logic

# toán tử so sánh
x = int (input ("Nhập số x:"))
y = int (input ("Nhập số y:"))
print ("{0} > {1} là {2}".format(x,y,x > y))
print ("{0} < {1} là {2}".format(x,y,x < y))
print ("{0} >= {1} là {2}".format(x,y,x >= y))
print ("{0} <= {1} là {2}".format(x,y,x <= y))
print ("{0} != {1} là {2}".format(x,y,x != y))
print ("{0} == {1} là {2}".format(x,y,x == y))
# toán tử logic
print ("Đáp án của x > y và x < y:",(x > y and x < y))
print ("Đáp án của x > y hoặc x < y:",(x > y or x < y))
print ("Đáp án của x > y hoặc x != 5:",(x > y or x != 5))
print ("Đáp án của x < y và x == 10:",(x < y and x == 10))
print ("Đáp án của x không phải lớn y", (not (x > y)))