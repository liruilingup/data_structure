'''
53. 最大子数组和 (普通数组)
'''
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
out_put = 6
def subarraySum(nums):
    """
    请你统计并返回 该数组中和为 k 的子数组的个数
    """
    res = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        res[i] = max(nums[i], res[i-1] + nums[i])
        
    return max(res)
print(subarraySum(nums))


