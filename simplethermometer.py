x=input('insert any value of c and f')
unit=x[-1]
x=int(x[0:-1])

if ((unit=='c')|(unit=='C')):
    x=round(x*(9/5)+32)
    print(str(x)+'F')
elif ((unit=='f')|(unit=='F')):
    x=round((x-32)*(5/9))
    print(str(x)+'C')    