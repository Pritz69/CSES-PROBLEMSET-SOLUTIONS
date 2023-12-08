-->https://cses.fi/problemset/task/1092/



n=int(input())
ans=(n*(n+1))//2
if ans%2==1 :
    print("NO")
else :
    print("YES")
    l1=[]
    l2=[]
    if n%2==0:
        for i in range(1,(n//2)+1,2) :
            l1.append(i)
            l1.append(n-i+1)
        for j in range(2,(n//2)+1,2) :
            l2.append(j)
            l2.append(n-j+1)
    else :
        t=n-1
        for i in range(1,(t//2)+1,2) :
            l1.append(i)
            l1.append(t-i+1)
        for j in range(2,(t//2)+1,2) :
            l2.append(j)
            l2.append(t-j+1)
        if (len(l1)<len(l2)) :
            l1.append(n)
        else :
            l2.append(n)
    print(len(l1))
    s1=""
    for x in l1 :
        s1 += str(x) +" "
    print(s1)
    print(len(l2))
    s2=""
    for x in l2 :
        s2 += str(x) +" "
    print(s2)
