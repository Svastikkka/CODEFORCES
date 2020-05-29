T = int(input())
for i in range(0,T):
    a,b,c=list(map(int,input().split()))
    while a>0 and b and a/2+10<a:
        b=b-1
        a=a/2+10
    if a<=c*10:
        print("YES")
    else:
        print("NO")