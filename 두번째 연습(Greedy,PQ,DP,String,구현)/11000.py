# 0803
# 강의실 배정
# idea : 시간 단축을 위해 우선순위 큐를 사용하자
import heapq
import sys

table = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))])

heap = []
heapq.heappush(heap, table[0][1])
for i in range(1, len(table)):
    # 시작 시간이 작으면 같은 강의실에서 할 수 없다.
    if heap[0] > table[i][0]:
        heapq.heappush(heap, table[i][1])
    # 시작 시간이 크거나 같으면 같은 강의실에서 할 수 있다.
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, table[i][1])
print(len(heap))