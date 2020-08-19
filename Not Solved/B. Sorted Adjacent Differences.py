t = int(input())
while t:
    t -= 1
    n =int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = []
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[n-i-1])
    if n&1: ans.append(a[n//2])
    ans.reverse()
    print(*ans)