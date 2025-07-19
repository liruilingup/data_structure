nums = [1,8,6,2,5,4,8,3,7]
res = 49 

def maxArea(height):
    """
    11. 盛最多水的容器
    """
    i, j = 0, len(nums)-1
    tmp = 0
    result = 0
    while i<j:
        
        if nums[j] > nums[i]:
            tmp = min(nums[j], nums[i]) * (j-i)
            i+=1
        else:
            tmp = min(nums[j], nums[i]) * (j-i)
            j -= 1
        result = max(result, tmp)
            
        
    print(result)

maxArea(nums)


def maxArea2(height):
    if len(height) == 1: return 1
    i = 0
    j = len(height) - 1
    result = 0
    while i < j:
        tmp = (j-i) * min(height[i], height[j])
        result = max(result, tmp)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return result

print(maxArea2(nums))

