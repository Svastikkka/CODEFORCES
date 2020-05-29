x,y = list(map(int,input().split()))
s= list(input())
for i in range(0,len(s)):
    if s[i] is "U":
        y=y+1
    elif s[i] is "D":
        y=y-1
    elif s[i] is "L":
        x=x-1
    elif s[i] is "R":
        x=x+1
print(x,y)

