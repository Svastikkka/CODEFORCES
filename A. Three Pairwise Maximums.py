t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    res=sorted(l,reverse=True)
    a=max(res)
    b=min(res)
    c=1
    if res[0]==max(a,b) and res[1]==max(a,c) and res[2]==max(b,c):
        print("YES")
        print(a,b,c)
    else:print("NO")


