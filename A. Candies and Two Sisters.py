T=int(input())
for i in range(0,T):
    a=int(input())
    if a%2 != 0:
        r=a/2
    elif a%2 ==0:
        r=a/2
        r=r-1
    elif a==0 or a==1 or a==2:
        r=0
    print(int(r))
