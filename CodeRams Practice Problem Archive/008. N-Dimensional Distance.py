import math

t=int(input())
res=0
for i in range(t):
    p=int(input())
    q=int(input())
    res=res+abs((p-q)**2)
print(math.sqrt(res))