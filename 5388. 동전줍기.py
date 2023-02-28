##KT aivle school 코딩마스터스 5388 동전 줍기 문제 풀이

# height : 산의 높이, coins : 각 위치 동전 개수
height = int(input())
coins = []
for i in range(height):
    coins.append(list(map(int, input().split())))

# dp: 각 위치에서 얻을 수 있는 최대 동전 합
dp = [0 for i in range(height)]
dp[0] = coins[0][0]

for i in range(1, height):
    for j in range(i, -1, -1):
        if j == i:
            dp[j] = dp[j-1] + coins[i][j]
        elif j == 0:
            dp[j] = dp[j] + coins[i][j]
        else:
            dp[j] = max(dp[j-1], dp[j]) + coins[i][j]

print(max(dp))
