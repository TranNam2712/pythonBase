# Luyện tập:
import random

# bài 1:
"""
    in hình sau:
    x x x x x
      x     
        x
          x
    x x x x x
    với n là số tùy ý
"""
n = int (input ("Nhập giá trị n:"))
for i in range (0,n,1):
    for j in range (0,n,1):
        if (i == 0 or i == n-1):
            print ("x",end="")
        else:
            if (i == j):
                print ("x",end="")
            else:
                print (" ",end ="")
    print ()

# bài 2:
"""
    in hình sau:
    x x x x x
      x x x
        x
    với n là một số lẻ
"""
n = int (input ("Nhập vào 1 số lẻ:"))
while (n %2 == 0):
    print (n,"không phải số lẻ")
    n = int (input ("Nhập lại giá trị:"))
for i in range (0,n,1):
    for j in range (0,n,1):
        if (i == 0):
            print ("x",end="")
        else:
            if (j == i):
                for k in range (j,n-i,1):
                    print ("x",end="")
                    if (k == n-i-1):
                        print ()
                break  
            else:
                print (" ",end="")
    if (i == 0):
        print ()


# bài 3:
"""
    in hình sau:
    x x x x x x x
    x x       x x
    x x x   x x x
    x x x x x x x
    x x x   x x x
    x x       x x
    x x x x x x x
    với n là 1 số lẻ
"""
print ()
for i in range (0,n,1):
    for j in range (0,n,1):
        # điều kiện nãy sẽ in ra các số ở hàng đầu,cuối và giữa
        if (i in [0,n-1,(n//2)]):
            print ("x",end="")
        else:
            # nếu không phải 3 điều kiện trên thì:
            """
                ta sẽ lấy điểm trên đường chéo chính để làm điểm kết thúc của nhánh trái
                và ta sẽ lấy điểm trên đường chéo phụ làm điểm bắt đầu và đi tới n
            """
            if ((j <= i and i < (n//2)) or (j > (n//2) and j>=n-1-i)
                ):
                print ("x",end="")
            else:
                # lúc này i > đường giữa:
                """
                    ta sẽ dựa theo số lần in của bên phải và giả lập nó qua bên trái sau đó ta trừ ra số lượng của 2 cánh để tính khoảng trống. Cuối cùng ta in ra số lượng y như số lượng giả lập
                """
                if (i > n//2):
                    count = 0
                    for k in range (i,n,1):
                        count+=1
                        print ("x",end="")
                    for k in range (0,n-count*2,1):
                        print (" ",end="")
                    for k in range (0,count,1):
                        print ("x",end="")
                    break
                else:
                    print (" ",end="")
    print ()

# bài 4:
"""
    in hình sau:
          x
        x x x   
      x x x x x
    x x x x x x x
      x x x x x
        x x x
          x
    với n là một số lẻ
"""
space = 2
for i in range (0,n,1):
    for j in range (0,n,1):
        if (i < n//2):
            if (j == n//2 - i):
                for k in range (n//2-i,n//2+i+1,1):
                    print ("x",end="")
            else:
                print (" ",end="")
        elif (i > n//2):
            start = i - n//2
            end = n - start
            for k in range (0,space//2,1):
                print (" ",end="")
            for k in range (start,end,1):
                print ("x",end="")
            space += 2
            break
        else:
            print ("x",end="")
    print ()

# bài 5:
"""
    Cho một số được random ngẫu nhiên, hãy nhập vào một giá trị n, sau đó từ giá trị đó tìm ra con số random đó một cách ngắn nhất (số được random là một con số bí mật)
"""
hiddenValue = random.randint (0,1000)
n = int (input ("Nhập giá trị dự đoán:"))
canDuoi = 0
canTren = 1000
# hidden = 13, n = 93
"""
(0,92) => n = 46
(0,45) => n = 22
(0,21) => n = 10
(11,21) => n = 16
(11, 16) => n = 13
"""
while (n != hiddenValue):
    if (n > hiddenValue):
        print (n,"đang lớn hơn giá trị ẩn")
        canTren = n-1
        n = (canDuoi + canTren)//2
    elif (n < hiddenValue):
        print (n, "đang bé hơn giá trị ẩn")
        canDuoi = n + 1
        n = (canDuoi + canTren)//2
print ("Giá trị ẩn là:",hiddenValue)
print ("Giá trị tìm thấy là:",n)