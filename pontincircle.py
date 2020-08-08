import math
x=float(input("x:"))
y=float(input("y:"))
r=float(input("r:"))
hyp=math.sqrt(pow(x,2)+pow(y,2))
if hyp<=r:
    print("the pont belongs in circle")
else:
    print("outside the circle")