# vòng lặp for trong python

# ---xuất ra khoảng giá trị của i---
for i in range (10):
    print (i,end = " ") # vòng for này có nghĩa là sẽ chạy từ 0 đến 9
# ---xuất ra 10 lần Hello---
print () # xuống 1 dòng
for i in range (10):
    print ("hello") # đoạn lệnh này có nghĩa là nó sẽ chạy từ i = 0, điều kiện là i<10. Sau khi thực hiện đoạn lệnh sau i+=1. Nếu điều kiện còn đúng thì sẽ còn thực hiện
# ---xuất ra tổng từ 1 đến n---
n = int (input ("Nhập số n:"))
s = 0
for i in range (n + 1):
    s += i # đoạn lệnh này sẽ chạy từ 0 cho đến n+1. Nếu i<n+1 (i<=n) thì lệnh còn được thực thi
print ("Tổng là:",s) # ta có thể sử dụng công thức: s = (n*(n+1)) / 2
# ---in ra các số chẵn nằm trong khoảng từ 1 đến n (cách không dùng bước nhảy)---
for i in range (n+1):
    if i%2 == 0:
        print (i,end=" ")
print ()
# ---in ra các số chẵn nằm trong khoảng từ 1 đến n (dùng bước nhảy)---
for i in range (0,n+1,2):
    print (i,end=" ")
print ()
# --- in ra tất cả phần tử trong mảng---
colors = ["Đỏ","Tím","Vàng","Lục","Lam","Chàm","Tím"]
for i in range (len(colors)):
    print (colors[i])
# hoặc
for color in colors:
    print (color)
# ---in ra bảng cửu chương từ 1 đến n---
n = int (input ("Nhập số bảng cửu chương muốn in:"))
for i in range (1,n+1,1):
    print ("Bảng cửu chương",i)
    for j in range (1,11,1):
        print ("{0} x {1} = {2}".format (i,j,i*j))
    print ()
