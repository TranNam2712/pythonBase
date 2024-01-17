# dictionary

# khai báo 1 từ điển
sinhVien = {
    "hoTen" : "Trần Nhật Nam",
    "maLop" : "001",
    "khoa" : "Công nghệ thông tin"
}
print (sinhVien) # in hết thông tin sinhVien
print (sinhVien["hoTen"]) # in họ tên sinhVien
# lấy ra khoa bằng key gán vào 1 biến
khoa = sinhVien.get ("khoa")
print (khoa)
# thay đổi giá trị
sinhVien["hoTen"] = "Trần Văn B" # cách 1
sinhVien.update ({"khoa" : "Quản trị kinh doanh"}) # cách 2
print (sinhVien)
# thêm các mục
sinhVien["namHoc"] = 2023 # cách 1
print (sinhVien)
sinhVien.update ({"noiSinh" : "Long Khánh"}) # cách 2
print (sinhVien)
# loại bỏ 1 mục được chỉ định
sinhVien.pop ("namHoc")
print (sinhVien)
# loại bỏ 1 mục cuối cùng
sinhVien.popitem ()
print (sinhVien)
# làm trống từ điển
sinhVien.clear ()
# xóa bỏ toàn bộ từ điển
# del sinhVien
print (sinhVien)
# duyệt qua giá trị
giangVien = {
    "chuyenNganh" : "Khoa học máy tính",
    "soNamKinhNghiem" : 5,
    "khoa" : "Công nghệ thông tin"
}
for x in giangVien.values ():
    print (x)
# duyệt qua khóa
for key in giangVien.keys ():
    print (key)
# duyệt qua cặp giá trị
for key,value in giangVien.items ():
    print (key,value)