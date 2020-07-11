print("hello!\n")
#write a comment
var1 = 1 #int
var2 =3.4 #float
var3 ="abcd" #string
var4 = True #bool
var5 ="4" #here 4 is considered as a string as it is defined in double quotes
print("var2=",var2)
print("datatype:",type(var2))
print("the sum is:",var1+var2)
print("the concat:",var5+var5)
print("explicit casting",var1+int(var5))

"""
this is a
multiline comment
"""
#Arithmetic operation
a=2
b=3
print("add",a+b)
print("sub",a-b)
print("mul",a*b)
print("div",a/b)
print("mod",a%b)
print("exponential",a**b)
print("div with int output",a//b)#floor division
print(a is b)
x=True
y=False
print(x and y)
print(x or y)
print("bye for now!", end="everyone\n")
print("variable and datatype")
A =input("enter your name")
print(A, end=" ")
# now solve day1 programs
A="1234567"
A[1::2]