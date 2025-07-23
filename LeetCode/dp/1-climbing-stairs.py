'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''

n = 10
def climbStairs(n):
    def dfs(i):
        if i == 1 or i == 2:
            return i
        else:
            return dfs(i-1) + dfs(i-2)
    return dfs(n)



print(climbStairs(n))



