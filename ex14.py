# Chương trình rút thăm trúng thưởng

# yêu cầu:
"""
1. thêm thăm vào thùng
2. xóa thăm khỏi thùng
3. bốc 1 số ngẫu nhiên để nhận thưởng
"""
import random

thamTrungThuong = set ()
while (True):
    choice = int (input ("Nhập vào lựa chọn của bạn:"))
    if choice == 1:
        maTham = input ("Nhập mã thăm trúng thưởng thêm vào thùng:")
        thamTrungThuong.add (maTham)
    elif choice == 2:
        maTham = input ("Nhập mã thăm muốn xóa:")
        thamTrungThuong.discard (maTham)
    elif choice == 3:
        if (len (thamTrungThuong) > 0):
            i = random.randint (0,len(thamTrungThuong)-1)
            j = 0
            for maTrungThuong in thamTrungThuong:
                if (i == j):
                    print ("Mã trúng thưởng là:",maTrungThuong,"xin chúc mừng!")
                    thamTrungThuong.remove (maTrungThuong)
                    break
                j+=1
    else:
        print ("Xin nhập đúng lựa chọn")
    if (len (thamTrungThuong) == 0):
        print ("Hiện không có thăm nào")
    else:
        print ("Thăm hiện tại: ", thamTrungThuong)
