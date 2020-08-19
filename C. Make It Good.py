for i in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    c=n-1
    while c>0 and m[c-1]>=m[c]:c-=1
    while c>0 and m[c-1]<=m[c]:c-=1
    print(c)