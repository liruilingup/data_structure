
"""
121. 买卖股票的最佳时机
"""

def maxProfit(prices):
    profit = 0
    low = float('inf')
    for i in prices:
        low = min(i, low)
        profit = max(profit, i-low)
    
    return profit


print(maxProfit([7,1,5,3,6,4]))

