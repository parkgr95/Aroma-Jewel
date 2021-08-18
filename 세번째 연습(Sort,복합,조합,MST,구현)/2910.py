import sys

n, c = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

# 딕셔너리 자료형으로 각 수의 등장 횟수 저장
count = {}
for x in data:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
# 등장 횟수대로 저장
count = sorted(count.items(), key=lambda x: -x[1])

# 등장 횟수만큼 출력
answer = []
for i, j in count:
    answer += [i]*j

print(*answer)