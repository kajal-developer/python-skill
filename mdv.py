mdv=input("calculate(m,d,v):")
if mdv=='m':
    d=float(input("enter density:"))
    v=float(input("enter volume:"))
    result=d*v
elif mdv=='d':
    m=float(input("enter mass:"))
    v=float(input("enter volume:"))
    result=m/v
else:
    m=float(input("enter mass:"))
    d=float(input("enter density:"))
    result=m/d

print(result)