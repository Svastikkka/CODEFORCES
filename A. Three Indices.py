def solve(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            print("YES")
            print(i, i + 1, i + 2)
            return

    print("NO")


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(arr)