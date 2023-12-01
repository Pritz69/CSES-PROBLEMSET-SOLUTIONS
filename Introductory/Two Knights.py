-->https://cses.fi/problemset/task/1072/



n=int(input())
def f(x) :
    if n==0 :
        return 1
    l=[1,1]
    for i in range(2,x+1) :
        l.append(l[i-1]*i)
    return l[x]
def cmb(x,r) :
    num=f(x)
    den=f(x-r)*f(r)
    return num//den
for i in range(1,n+1) :
    #totalways=cmb(i*i,2)
    totalways=((i*i)*((i*i)-1))//2
    atkways=2*2*(i-1)*(i-2)
    print(totalways-atkways)
