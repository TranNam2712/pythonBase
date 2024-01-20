# ghi chú trên 1 dòng

"""
ghi chú trên nhiều dòng
example 1
example 2
example 3
"""

# cách in ra màn hình

# in ra tên người dùng
print ("Trần Nhật Nam")
# in ra tên người dùng và số
print ("Trần Nhật Nam, tuổi:", 20)
# in ra chuỗi bằng nhiều tham số truyền vào(các tham số truyền vào sẽ được ngăn cách bởi 1 khoảng trắng bởi được sep mặc định)
print ("Trần","Nhật","Nam","tuổi:",20,"giới tính:","Nam","năm sinh: ",2004)
# in ra chuỗi với các tham số truyền vào ngăn cách là ","
print ("Trần Nhật Nam","tuổi: 20","năm sinh: 2004",sep=",")
# thông thường các chuỗi được set end mặc định là "\n", bây giờ sẽ set lại là một chuỗi bất kì (ví dụ "abc")
print ("Trần Nhật Nam", end = "abc")
print ("Trần Nhật Nam",end = "\n") # \n là kí tự xuống dòng
# format một chuỗi
print ("Tên:{0},Quốc tịch:{1}".format ("Trần Nhật Nam","Việt Nam"))
print ("Tên:{0},tuổi:{1}".format ("Trần Nhật Nam",20))

# cách nhập dữ liệu từ bàn phím

# khởi tạo 1 biến và nhập dữ liệu vào sau đó xuất ra màn hình
a = input("Nhập vào số a: ")
b = input()
print (a)
print (b)
print (a + b)
ho = input ("Nhập vào họ: ")
ten = input ("Nhập vào tên: ")
print ("Họ: {0},Tên: {1}".format (ho,ten))
