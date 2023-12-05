--->https://cses.fi/problemset/task/1084/


n,m,k=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
l.sort()
s.sort()
i = 0
j = 0
c = 0
while i < n and j < m:
    if s[j] <= (l[i] + k) and s[j] >= (l[i] - k):
        c += 1
        i += 1
        j += 1
    elif l[i] > s[j]:
        j += 1
    else:
        i += 1
print(c)
