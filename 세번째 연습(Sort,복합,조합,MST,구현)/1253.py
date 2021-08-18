import sys

n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))

ans = 0
for i in range(n):
    tmp = arr[:i] + arr[i + 1:]
    start, end = 0, n - 2
    while start < end:
        mid = tmp[start] + tmp[end]
        if mid == arr[i]:
            ans += 1
            break
        if mid < arr[i]:
            start += 1
        else:
            end -= 1

print(ans)