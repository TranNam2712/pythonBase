# kiểu String trong python

# một chuỗi nhiều dòng
chuoiNhieuDong = '''
Dòng 1
Dòng 2
Dòng 3
'''
print (chuoiNhieuDong)
# in ra dòng chữ hello 5 lần
hello = "Hello\n"
hello5Lan = hello * 5
print (hello5Lan)
# kiểm tra chuỗi con có nằm trong chuỗi cha hay không
chuoiCha = "Trường đại học Sài Gòn"
chuoiCon1 = "đại học Sài Gòn"
chuoiCon2 = "đại học Tài chính"
if chuoiCon1 in chuoiCha:
    print ("chuỗi con thứ 1 nằm trong chuỗi cha")
else:
    print ("chuỗi con thứ 1 không nằm trong chuỗi cha")
# viết hoa kí tự đầu tiên của chữ đầu tiên trong chuỗi và các từ kế tiếp sẽ bị viết thường kí tự đầu
s = "hôm Nay Trời đẹp quá"
s = str.capitalize (s)
print (s) # Hôm nay trời đẹp quá
# viết hoa toàn bộ kí tự trong chuỗi
s = "trần nhật nam"
s = s.upper ()
print (s) # TRẦN NHẬT NAM
# viết thường toàn bộ kí tự trong chuỗi
s = "TRẦN NHẬT NAM"
s = s.lower ()
print (s) # trần nhật nam
# tìm và trả về vị trí chuỗi con, đếm số lần chuỗi xuất hiện
s = "Hôm nay trời đẹp quá"
sCon1 = "trời"
sCon2 = "mưa"
print (s.find (sCon1)) # 8
print (s.count (sCon1)) # 1
print (s.find (sCon2)) # -1
print (s.count (sCon2)) # 0
# thay thế chuỗi
s = "Hôm nay trời không có mưa"
s = s.replace ("mưa","MƯA")
print (s)
# cắt chuỗi
s = "Hôm nay trời đẹp quá"
listOfS = s.split (" ") # cắt thông qua dấu " "
print (listOfS) # ['Hôm', 'nay', 'trời', 'đẹp', 'quá']
for str in listOfS:
    print (str)