a=0;b=0;c=0;d=0;e=0
x=int(input())
y=list(input())
for i in range(0,x):
    if y[i] is "a":
        a=a+1
    elif y[i] is "b":
        b=b+1
    elif y[i] is "c":
        c=c+1
    elif y[i] is "d":
        d=d+1
    elif y[i] is "e":
        e=e+1
print(min(a,b,c,d,e),max(a,b,c,d,e))

