# chuyển đổi số thập phân sang nhị phân

soThapPhan = int (input ("Nhập vào số thập phân:"))
while soThapPhan < 0:
    print ("số phải lớn hơn 0")
    soThapPhan = int (input ("Nhập lại số thập phân:"))
soNhiPhan = ""
while soThapPhan > 0:
    soNhiPhan = str(soThapPhan%2) + soNhiPhan
    soThapPhan //= 2
print (soNhiPhan)
