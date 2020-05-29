x=int(input())
y=sorted(list(map(int,input().split())))
count=0

for i in range(len(y)-1):
    if y[i]==y[i+1]:
        count=count+1
print((count+len(y))%1000000007)






