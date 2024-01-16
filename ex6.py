# xác định tam giác và tính chu vi, diện tích (giả sử: các cạnh là số nguyên)

# gợi ý: công thức Heron tính diện tích: S = sqrt (p*(p-a)*(p-b)*(p-c)) trong đó p là nửa chu vi. Công thức này dùng đối với tất cả tam giác

import math

print ("Nhập vào 3 cạnh của tam giác:")
a = int (input ("Nhập vào cạnh 1:"))
b = int (input ("Nhập vào cạnh 2:"))
c = int (input ("Nhập vào cạnh 3:"))

chuVi = 0
dienTich = 0

if a <= 0 or b <= 0 or c <= 0:
    print ("Đây không phải tam giác")
else:
    chuVi = a + b + c
    p = chuVi/2
    dienTich = math.sqrt (p * (p-a) * (p-b) * (p-c))
    if a == b == c:
        print ("Đây là tam giác đều")
    elif a == b or a == c or b == c:
        print ("Đây là tam giác cân")
    else:
        if pow (a,2) == (pow(b,2) + pow(c,2)) or pow (b,2) == (pow(a,2) + 
        pow(c,2)) or pow (c,2) == (pow(b,2) + pow(a,2)):
            print ("Đây là tam giác vuông")
        else:
            print ("Đây là tam giác thường")

print ("Chu vi là: ",chuVi)
print ("Diện tích là: ",dienTich)