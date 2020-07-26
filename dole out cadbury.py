def count(a,b):
    minimum=min(a,b)
    maximum=max(a,b)

    i=(minimum,maximum)
    if i in D:
        return D[i]
    
    if minimum==0:
        return 0
    if minimum==1:
        return a*b
    
    chocolate=maximum//minimum
    new_side=maximum%minimum
    chocolate+=count(new_side,minimum)

    D[i]=chocolate
    return chocolate

D={}
p=int(input())
q=int(input())
r=int(input())
s=int(input())

ans=0
for i in range(p,q+1):
    for j in range(r,s+1):
        ans+=count(i,j)
print(ans)