x,y=list(map(int,input().split()))
arr=[]
count=0
for i in range(0,x):
    element=list(map(str,input().strip()))
    arr.append(element)
    count+=arr[i].count('x')
print(count)
