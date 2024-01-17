# bài tập tra từ điển

"""
    1. thêm 1 từ vận và kèm nghĩa của chúng
    2. tra cứu ý nghĩa của chúng
    3. cập nhật ý nghĩa cho 1 từ vận
    4. xóa đi 1 từ vận
    5. xóa toàn bộ từ vận
    6. kết thúc
"""

sachTuDien = dict()

while (True):
    choice = int (input ("Nhập lựa chọn:"))
    if (choice == 1):
        eng = input ("Nhập từ vận:")
        vn = input ("Nhập nghĩa của chúng:")
        sachTuDien.update ({eng : vn})
    elif (choice == 2):
        eng = input ("Nhập từ muốn tra cứu:")
        if eng in sachTuDien.keys ():
            print ("Nghĩa:",sachTuDien[eng])
    elif (choice == 3):
        eng = input ("Nhập từ vận muốn cập nhật:")
        vn = input ("Cập nhật nghĩa mới:")
        sachTuDien.update ({eng : vn})
    elif (choice == 4):
        eng = input ("Nhập từ vận cần xóa:")
        sachTuDien.pop (eng)
    elif (choice == 5):
        sachTuDien.clear ()
    else:
        break
    print ("danh sách từ vận:",sachTuDien)