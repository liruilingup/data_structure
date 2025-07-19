nums = [0,1,0,3,12]


def moveZeroes(nums):
    """
    283. 移动零
    """
    j = 0
    for k in nums:
        if k != 0:
            nums[j] = k
            j += 1
    for m in range(j ,len(nums)):
        nums[m] = 0

    print(nums)

moveZeroes(nums)



