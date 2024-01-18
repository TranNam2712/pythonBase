# hàm (function)

# viết hàm in ra câu xin chào
def xinChaoKhongThamSo ():
    print ("Hello")
# viết hàm in ra câu xin chào có đối số
def xinChaoTen (hoVaTen):
    print ("hello",hoVaTen)
def intro (hoTen,tuoi):
    print ("hello, tôi tên là",hoTen,"năm nay tôi",tuoi,"tuổi")
# khi không xác định được có bao nhiêu đối số
def thoiKhoaBieu (*monHoc):
    print ("Môn 1:", monHoc[0])
    print ("Môn 2:", monHoc[1])
def tong (*giaTri):
    sum = 0
    for x in giaTri:
        sum += x
    print (sum)
# truyền nhiều đối số xác định thông qua tên
def xinChao (**ten):
    print ("Họ:",ten["ho"])
    print ("Tên lót:",ten["tenLot"])
    print ("Tên:",ten["ten"])
# dùng return để trả về giá trị
def tongChan (n): # tổng các số chẵn
    sum = 0
    for i in range (2,n+1,2):
        sum += i
    return sum
def tichCacSo (*giaTri): # tích các số
    x = 1
    for i in giaTri:
        x *= i
    return x
def uocChungLonNhat1 (a,b): # tìm ước chung lớn nhất của 2 số (có nhiều cách)
    if (a == 0 or b == 0):
        return a+b
    else:
        giaTriBeNhat = min (a,b)
        uoc = 0
        for i in range (1,giaTriBeNhat+1,1):
            if (a %i == 0 and b %i == 0):
                uoc = i
        return uoc
def uocChungLonNhat2 (a,b):
    if (a == 0 or b == 0):
        return a + b
    else:
        while (a != b):
            if (a > b):
                a -= b
            else:
                b -= a
        return a
def tongLe (n):
    sum = 0
    for i in range (1,n+1,2):
        sum += i
    return sum
# nhập 1 dãy n số từ bàn phím tính tổng
def nhap (listNumber,n):
    for i in range (0,n,1):
        listNumber.append (int (input ()))
def tongMang (listNumber,n):
    sum = 0
    for i in range (0,n,1):
        sum += listNumber[i]
    return sum
xinChaoKhongThamSo ()
xinChaoTen ("Trần Nhật Nam")
intro ("Trần Nhật Nam",19)
thoiKhoaBieu ("Toán","Lý","Hóa","Sinh")
xinChao (ten = "Nam",tenLot = "Nhật",ho = "Trần")
tong (1,3,4,5,6,7)
print ("Tổng các số chẵn là:",tongChan (10))
print ("Tổng các số lẻ là:",tongLe (10))
print ("Tích của:",tichCacSo (2,3,4,5))
print ("Ước chung lớn nhất là:",uocChungLonNhat1 (35,77))
print ("Ước chung lớn nhất là:",uocChungLonNhat2 (11,121))
arr = list () # hoặc: arr = []
nhap (arr,10)
print ("Tổng các phần tử trong mảng:",tongMang (arr,10))