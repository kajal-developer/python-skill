a=max(420,130)
b=min(420,130)
q=0
r=1
while r>0:
    q=a/b
    r=a%b
    if r==0:
        print(b)
        break
    else:
        a=b
        b=r
i=int(input("enter i="))
j=int(input("enter j="))
x=min(i,j)
while(1):
    if(x%i==0 and x%j==0):
        print(x)
        break
    x=x+1
    





