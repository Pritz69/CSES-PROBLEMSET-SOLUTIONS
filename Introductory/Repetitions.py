-->https://cses.fi/problemset/task/1069/


s=input()
m=1
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1] :
        c +=1
        m=max(m,c)
    else :
        c =1
print(m)
