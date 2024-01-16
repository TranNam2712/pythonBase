# giải phương trình bậc 2
import math

print ("Cấu trúc: ax2 + bx + c = 0")
a = float (input ("Nhập số a:"))
b = float (input ("Nhập số b:"))
c = float (input ("Nhập số c:"))
# x = 0

if a == 0:
    if b == 0:
        print ("Vô số nghiệm") if (c == 0) else print ("Vô nghiệm")
    else:
        print ("x=",-c/b)
else:
    delta = math.pow (b,2) - 4*a*c
    if delta < 0:
        print ("Phương trình vô nghiệm")
    elif delta > 0:
        print ("x1=",(-b + math.sqrt (delta)) / 2*a)
        print ("x2=",(-b - math.sqrt (delta)) / 2*a)
    else:
        print ("có nghiệm kép là:",-b/2*a)

# bộ test:
"""
    x2 - 4x + 3 = 0 (x = 1, x = 3)
    x2 + 6x + 9 = 0 (x = -3)
    2x2 + 5x + 2 = 0 (x = -0.5, x = -2)
    x2 -2x + 1 = 0 (x = 1)
"""