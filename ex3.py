# toán tử gán trong python
a = 5
b = 4
print ("{0} += {1} = {2}".format (a,b,a + b))
print ("{0} -= {1} = {2}".format (a,b,a - b))
print ("{0} /= {1} = {2}".format (a,b,a / b))
print ("{0} *= {1} = {2}".format (a,b,a * b))
print ("{0} %= {1} = {2}".format (a,b,a % b))
print ("{0} **= {1} = {2}".format (a,b,a ** b))
print ("{0} //= {1} = {2}".format (a,b,a // b))

# thư viện math

import math
x = float (input ("Nhập giá trị x: "))
print ("|x|=",math.fabs (x))
print ("sqrt(x)=",math.sqrt (x))
print ("giá trị nhỏ nhất lớn hơn hoặc bằng x=",math.ceil (x))
print ("giá trị nhỏ nhất bé hơn hoặc bằng x=",math.floor (x))
print ("e mũ x=",math.exp (x))
print ("5 mũ x=",math.pow (5,x))
print ("log cơ số 5 = x thì số mũ =",math.log (x,5))

