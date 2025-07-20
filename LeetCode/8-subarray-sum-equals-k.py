''' 
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
'''
from collections import defaultdict  

nums = [1,1,1]
k = 2

# nums = [1,2,3]
# k = 3

# nums = [1,-1,0]
# k = 0

def subarraySum(nums, k):
    """
    暴力破解, 但是会超时
    """
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            if sum(nums[i:j + 1]) == k:
                count += 1
            else:
                continue

    return count


print(subarraySum(nums, k))



def subarraySum2(nums, k):
    """
    前缀和+哈希表：从两次遍历到一次遍历
    前缀和的定义：s[0]=0, s[i+1]=nums[0]+nums[1]+⋯+nums[i]。
    本质是对暴力算法的哈希表优化。
    """
    preSum = 0
    freq = {0: 1}
    cnt = 0

    for v in nums:
        preSum += v
        cnt += freq.get(preSum - k, 0)
        freq[preSum] = freq.get(preSum, 0) + 1

    return cnt
print(subarraySum2(nums, k))


def subarraySum3(nums, k):
    """
    前缀和+哈希表：从两次遍历到一次遍历
    前缀和的定义：s[0]=0, s[i+1]=nums[0]+nums[1]+⋯+nums[i]。
    本质是对暴力算法的哈希表优化。
    """
    s = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        s[i + 1] = s[i] + x

    ans = 0
    cnt = defaultdict(int)
    for sj in s:
        ans += cnt[sj - k]
        cnt[sj] += 1
    return ans

print(subarraySum3(nums, k))




def subarraySum4(nums, k):
    """
    自定义dict，设置默认值
    """
    # 先计算前缀和
    s = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        s[i + 1] = s[i] + x

    ans = 0
    cnt = {}
    for sj in s:
        ans += cnt.get(sj - k, 0)
        if cnt.get(sj, 0):
            cnt[sj] += 1
        else:
            cnt[sj] = 1
    print(cnt)
    return ans

print(subarraySum4(nums, k))




