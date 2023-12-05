n=int(input())
l=list(map(int,input().split()))
l.sort()
c=1
for i in range(1,n) :
    if l[i]!=l[i-1] :
        c +=1
#print(l)
print(c)
