''' 未排序的整数数组  '''
nums = [100,4,200,1,3,2]
def longestConsecutive(nums):
    """
    128. 最长连续序列
    """
    if not nums:return 0
    nums.sort()

    nums_sorted = sorted(nums)
    print(nums_sorted)
    count = 1
    max_lenth = 1
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] - nums_sorted[i-1] == 1:
            count += 1
            max_lenth = max(max_lenth, count)
        elif  nums_sorted[i] == nums_sorted[i-1]:
        	continue
        else:
            count = 1
    return max_lenth

print(longestConsecutive(nums))


def longestConsecutive2(nums):
    """
    使用哈希的解法
    """
    nums_dict = {}
    max_long = 0
    for num in nums:
        if nums_dict.get(num, None) is None:
            left = nums_dict.get(num-1, 0)
            right = nums_dict.get(num+1, 0)
            curent_long = 1 + left + right
            
            max_long = max(max_long, curent_long)
            nums_dict[num] = curent_long
            nums_dict[num - left] = curent_long
            nums_dict[num + right] = curent_long
    
    
    return max_long

print(longestConsecutive2(nums))
