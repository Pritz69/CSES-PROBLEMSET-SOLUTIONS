-->https://cses.fi/problemset/task/1071/


for i in range(int(input())):
    y,x=map(int,input().split())
    ans=0
    if y>x :
        if y%2==1 :
            ans=(y-1)**2 +1+(x-1)
        else :
            ans=y**2 - (x-1)
    else :
        if x%2==0 :
            ans=(x-1)**2 +1+(y-1)
        else :
            ans=x**2 - (y-1)
    print(ans)
