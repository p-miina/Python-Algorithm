from collections import deque
import sys

f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

distance = [0] * (n+1)
visited = [False] * (n+1)

ans = []

def bfs(start):
    q = deque([start])
    distance[start]=0
    visited[start]=True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                distance[i]=distance[now]+1
                if distance[i]==k:
                    ans.append(i)
    if len(ans)==0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)
            
bfs(x)
