x=int(input("enter abcissa:"))
y=int(input("enter ordinate:"))

if x>0 and y>0:
    print("quadrant1:",(x,y))
elif x<0 and y>0:
    print("quadrant2:",(x,y))
elif x<0 and y<0:
    print("quadrant3:",(x,y))
elif x>0 and y<0:
    print("quadrant4:",(x,y))
elif x==0 and y==0:
    print("point is at origin")
elif x==0:
    print("on y axis ",(x,y))
elif y==0:
    print("on x axis:",(x,y))