# 

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):

	hasmap = {}	
	for k, v in enumerate(nums):
		# print(k, v)
		if (target - v) in hasmap:
			return [k, hasmap[target - v]]
		else:
			hasmap[v] = k

print("使用哈希:", twoSum(nums, target))

def twoSum2(nums, target):
	"""
	使用循环
	"""
	for i in range(len(nums)):
		if target - nums[i] in nums:
			return [nums.index(target - nums[i]), i]
	return []


print("使用for循环:", twoSum2(nums, target))



