n=int(input())
ans=n*(n+1)//2
if ans%2==1 :
    print("NO")
else :
    print("YES")
    f=1
    s1=set()
    s1.add(n)
    s2=set()
    i=n-1
    while i > 0 :
        if f==0 :
            s1.add(i)
            i -=1
            if i!=0:
                s1.add(i)
            i -=1
            f=1
        else :
            s2.add(i)
            i -=1
            if i!=0:
                s2.add(i)
            i -=1
            f=0
    print(len(s1))
    print(' '.join(list(str(x) for x in s1)))
    print(len(s2))
    print(' '.join(list(str(x) for x in s2)))

#n=7
#743
#6521
#n=6
#6
#6 1
#5 2
#4 3
# 42//2=21
#n=8
#8541
#7632
