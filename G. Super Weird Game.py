m,n=list(map(int,input().split()))

MAcount=0
BAcount=0
MA=list(map(int,input().split()))
BA=list(map(int,input().split()))

for i in range(m-1):
    for j in range(i+1,m):
        if i<j:
            if MA[i] + MA[j] == n:
                MAcount += 1
            elif BA[i] + BA[j] == n:
                BAcount += 1
            else:
                continue


if MAcount > BAcount:
    print("MAHMOUD")
elif MAcount == BAcount:
    print("DRAW")
else:
    print("BASHAR")



