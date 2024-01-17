# set trong python

# tạo mới 1 set
monHoc = {"Toán", "Lý", "Hóa"}
# duyệt từng phần tử của môn học
for mon in monHoc:
    print ("Môn:",mon)
# thêm 1 phần tử (nếu thêm trùng thì nó vẫn thực hiện những không cộng dồn)
monHoc.add ("Lịch sử")
# monHoc.add ("Toán") # không thêm vào set
print (monHoc)
# thêm nhiều phần tử (có thể thêm list hoặc set đều được)
cacMon = ["Văn", "Anh văn", "Sinh"]
monHoc.update (cacMon)
print (monHoc)
# xóa phần tử
monHoc.remove ("Văn")
monHoc.discard ("Lịch sử")
print (monHoc)
# xóa phần tử đầu tiên
monHoc.pop ()
# làm rỗng set
monHoc.clear ()
