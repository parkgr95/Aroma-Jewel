# 0803
# 병든 나이트
# idea: 조건에 따라 구현하기
import sys

n, m = map(int, sys.stdin.readline().split())

if n == 1: # 세로가 한 칸일 경우 움직일 수 없다
    print(1)
elif n == 2: # 세로가 두 칸일 경우 오른쪽으로 두 칸씩만 움직일 수 있다. 그러므로 최대 이동거리는 (m-1)//2 + 1
    print(min(4, (m-1)//2 + 1))
else:
    if m < 7: # 세로가 두 칸일 경우 오른쪽으로 한 칸씩 움직일때 최대 이동횟수가 된다. 따라서 최대 이동거리는 m
        print(min(4, m))
    else: # 최대 이동 횟수는 두 칸씩 각각 한 번 움직인 횟수 + 처음 있던 칸과 두 칸씩 이동한 거리를 뺸 값
        print(2 + (m-5) + 1)