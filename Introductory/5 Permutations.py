-->https://cses.fi/problemset/task/1070/



n=int(input())
l=[]
if n==1 :
    print(1)
elif n<=3 :
    print("NO SOLUTION")
else :
    for i in range(2,n+1,2) :
        l.append(str(i))
    for i in range(1,n+1,2) :
        l.append(str(i))
    print(' '.join(l))
