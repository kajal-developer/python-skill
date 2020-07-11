#conditional statement
x=12
y=12
if x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
else:
    print("x is equal to y")
#nested if statement
a=41
if a>10:
    print("above 10")
    if a>20:
        print("above 20")
    else:
        print("but not above 20")

if a>20:
    pass      #pass is use to avoid an error as if statement is empty in this case
#loops
for i in range(10):
    print(i)
for j in range(3,10):
    print(j) #here loop will from 3 and end on 9
print("how to set interval in loop")
for k in range(3,30,3):
    print(k) #this loop will print 3 to 27 but with diff of 3
    #we can use else in loop
else:
    print("loop is ended")
print("nested for loop")
for p in range(6):
    for q in range(6-p):
        print(p)
#while loop
z=1
while z<5:
    print("the value of:",z)
    z+=1 #in this i++ is not used




