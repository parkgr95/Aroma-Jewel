import sys

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            if arr[:] not in result: result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

for i in range(int(sys.stdin.readline().rstrip())):
    data = sorted(list(sys.stdin.readline().rstrip()))
    p = sorted(permute(data))
    for x in p:
        print("".join(x))
