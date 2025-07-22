

n = 10
def climbStairs(n):
    def dfs(i):
        if i == 1 or i == 2:
            return i
        else:
            return dfs(i-1) + dfs(i-2)
    return dfs(n)



print(climbStairs(n))



