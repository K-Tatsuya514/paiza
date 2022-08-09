# coding: utf-8

N = int(input())
AB = [int(x) for x in input().split(" ")]
A = AB[0]
B = AB[1]

# 【条件】階段の段数：N、登り方：A段飛ばし、B段飛ばし

# dp：各段数にたどり着く登り方の種類
dp = [0 for x in range(N + 1)]

# dp[0]は開始時点の位置なので1とする
dp[0] = 1

# 登ることができない階の合計数
sum = 0

# 各段数にたどり着く登り方の種類数を格納していく
for i in range(1, N):
    if i >= A:
        dp[i] = dp[i] + dp[i-A]
    if i >= B:
        dp[i] = dp[i] + dp[i-B]
    if i <= N - B:
        dp[N] = 1
    if dp[i] == 0:
        sum += 1

# 各階の到達パターン数の表示
print(dp)

# 登ることができない階の合計数の表示
print(sum)
