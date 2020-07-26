num=int(input("enter num"))
rev=[]
while num>0:
    r=num%2
    rev.append(r)
    num=num//2 
    if num<1: 
       print("reverse binary is",rev)
       print("decimal to binary",rev[::-1])
       break
       
