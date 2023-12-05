-->https://cses.fi/problemset/task/1083/


n=int(input())
s=set(list(map(int,input().split())))
ans=0
for i in range(1,n+1) :
    if i not in s :
        ans=i
        break
print(ans)
