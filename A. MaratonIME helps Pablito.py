import math
T = int(input())
for i in range(0,T):
    a,b=list(map(int,input().split()))
    if math.gcd(a,b)>1:
        print("Sim")
    else:print("Nao")
