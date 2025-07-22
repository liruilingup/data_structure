
coins = [1, 2, 5]
amount = 11

def coinChange(coins, amount):
    dp = [inf]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i-coin>=0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[-1] if dp[-1]!=inf else -1



print(coinChange(coins, amount))