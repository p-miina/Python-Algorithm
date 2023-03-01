import sys
import heapq

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    # 편의점까지 거리, 포만감
    location, satisfaction = map(int, sys.stdin.readline().split())
    data.append([location, satisfaction])

# 편의점 거리 기준 오름차순 정렬
data.sort(key=lambda a: a[0])

# destination: 수민이의 위치(0)에서 목표지점인 식당까지의 거리
# p: 초기 수민이의 포만감
(destination, p) = map(int, sys.stdin.readline().split())

# 우선순위 큐 이용
queue = []
count = 0
idx = 0
while p < destination:
    while idx < n and data[idx][0] <= p:
        heapq.heappush(queue, [-data[idx][1], data[idx][0]])
        idx += 1
    if not queue:
        count = -1
        break
    p -= heapq.heappop(queue)[0]
    count += 1

print(count)
