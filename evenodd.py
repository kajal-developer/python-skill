def evenodd(num):
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")

evenodd(3)

x=int(input("first number is:"))
y=int(input("second number is"))
print("the maximum number is", end=" ")
if x>y:
    print(x)
else:
    print(y)


def divisiblity(a,b):

    if a%b==0:

        print(a,"is divisible by",b)
    else:
        print("not divisible")

divisiblity(20,2)