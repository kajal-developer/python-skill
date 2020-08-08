#handling error of a number can  not be divided by zero
a=int(input('num1:\t'))
b=int(input('num2:\t'))

try:
    c=a/b
except:
    print("you cannot divide ",a,'by',b)
else:
    print(c)