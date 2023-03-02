from collections import deque

n, m = map(int, input().split())
candy = list(map(int, input().split()))

c = deque(range(1, n + 1))

cnt = 0
for a in candy:
    if a not in c:
        continue

    idx = c.index(a)
    if idx >= len(c) - idx:
        cnt += len(c) - idx
        c.rotate(len(c) - idx)
    else:
        cnt += idx
        c.rotate(-idx)

    c.remove(a)

print(cnt)
