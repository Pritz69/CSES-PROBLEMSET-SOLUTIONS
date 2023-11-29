-->https://cses.fi/problemset/task/1094/


n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n) :
    if l[i]<l[i-1] :
        c += l[i-1]-l[i]
        l[i] = l[i-1]
print(c)
