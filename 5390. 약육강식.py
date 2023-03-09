n = int(input())

sharks = list(map(int, input().split()))

#dp[i] 값 1로 초기화(시작 상어 +1)
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if sharks[i] > sharks[j]:           # 현재 상어와 앞에 있는 상어의 크기 비교
            dp[i] = max(dp[i], dp[j]+1) # 현재 상어가 더 크면 앞의 상어 중 dp의 최대값에 1 더해줌 

print(max(dp))
