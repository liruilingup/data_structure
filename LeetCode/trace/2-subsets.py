nums = [1,2,3]

def subsets(nums):
    ans = []
    path = []
    n = len(nums)
    def dfs(i):
        ans.append(path.copy())  # 复制 path
        for j in range(i, n):  # 枚举选择的数字
            path.append(nums[j])
            dfs(j + 1)
            path.pop()  # 恢复现场
    dfs(0)
    return ans

print(subsets(nums))



