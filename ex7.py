# kiểu dữ liệu list

# tạo ra 1 list rỗng
emptyList = []
# tạo ra 1 đối tượng list rỗng
objEmptyList = list ()
# tạo ra list có dữ liệu
list1 = ["Đỏ","Vàng","Xanh"]
print (list1) # in tất cả phần tử trong danh sách
print (list1[0]) # in phần tử đầu tiên của danh sách (danh sách bắt đầu từ 0) cho đến n-1
list2 = [1,2,3,4,5,6,7,8]
print (list2[:]) # cũng là in ra tất cả phần tử trong danh sách
print (list2[0:3]) # in ra các phần tử nằm trong khoảng [0,3)
# thêm 1 phần tử vào cuối list
list3 = ["Đỏ","Cam","Lục","Lam"]
list3.append ("Chàm")
print (list3)
# thêm 1 phần tử vào 1 vị trí trong list
list3.insert (2,"Vàng")
print (list3)
# lấy độ dài của list
doDai = len (list3)
print ("Độ dài:",doDai)
# Đếm số lượng thỏa điều kiện trong list
list4 = ["Đỏ", "Xanh", "Vàng","Vàng","Xanh","Vàng"]
print ("Số lượng màu vàng: ",list4.count ("Vàng"))
print ("Số lượng màu đỏ: ",list4.count ("Đỏ"))
print ("Số lượng màu xanh: ",list4.count ("Xanh"))
# kiểm tra xem phần tử có nằm trong list hay không nếu có thì xóa phần tử ra khỏi list (chỉ xóa 1 phần tử nếu nhiều hơn)
if "Xanh" in list4:
    list4.remove ("Xanh") # nếu không kiểm tra mà giá trị không có trong danh sách thì sẽ lỗi
print (list4)
# xóa phần tử qua vị trí trong list
print (list4.pop (0)) # có thể xem phần tử lấy ra là phần tử nào
print (list4)
# đảo ngược list
list4.reverse ()
print (list4)
# sắp xếp list (theo kí tự Alpha nếu là chữ theo thứ tự tăng hoặc giảm nếu là số)
list4.sort ()
print ("Danh sách sau khi sắp xếp:",list4)
list5 = [5,4,7,2,8,0,9]
list5.sort () # sắp xếp tăng dần
print ("Danh sách sau khi sắp xếp: ", list5)
list5.sort (reverse=True) # sắp xếp giảm dần
print ("Danh sách sau khi sắp xếp: ", list5)
# xóa sạch phần tử trong list
list5.clear ()