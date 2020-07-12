
##not done
import math

N,M,Q=list(map(int,input().split()))
for i in range(N):
    A,B=list(map(int,input().split()))
    print(math.gcd(A,B))
    if A%2==0 and B%2==0:
        print(M-(math.gcd(A,B)/2)+1)
    elif A%2==0 and B%2!=0:
        print(M - math.gcd(A, B)*2)
    else:
        print(int(M-math.gcd(A,B)+1))
