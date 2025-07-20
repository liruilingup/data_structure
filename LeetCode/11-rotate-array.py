'''
189. 轮转数组
'''

nums = [1,2,3,4,5,6,7]
k = 3
# nums = [-1,-100,3,99]
# k = 2
# nums = [1,2]
# k = 2

out_put = [5,6,7,1,2,3,4]
def rotate(nums, k):
    """
    189. 轮转数组
    """
    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k %= n  # 轮转 k 次等于轮转 k % n 次
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

print(rotate(nums, k))

def rotate2(nums, k):
    """
    189. 轮转数组
    """
    for _ in range(k):
        nums.insert(0, nums.pop())
    return nums

print(rotate2(nums, k))

