from collections import deque

def solution(target, start):
    q = deque()
    q.append((start, 0)) # (현재 숫자, 횟수)
    visited = set()
    visited.add(start)
    
    while q:
        curr, count = q.popleft()
        
        if curr == target:
            return count
        
        if curr * 2 <= target * 2 and curr * 2 not in visited: # 2를 곱하는 경우
            q.append((curr * 2, count + 1))
            visited.add(curr * 2)
        
        if curr + 1 <= target and curr + 1 not in visited: # 1을 더하는 경우
            q.append((curr + 1, count + 1))
            visited.add(curr + 1)
        
        if curr - 1 > 0 and curr - 1 not in visited: # 1을 빼는 경우
            q.append((curr - 1, count + 1))
            visited.add(curr - 1)
            
a, b = map(int, input().split())
print(solution(a,b))
