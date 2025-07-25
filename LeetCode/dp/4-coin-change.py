'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

'''

'''
示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
'''

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