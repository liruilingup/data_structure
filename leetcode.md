### Array

##### 删除排序数组中的重复项

- 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度


```python
nums = [0,0,1,1,1,2,2,3,3,4]
count = 1
for i in range(len(nums) -1 ):
    if nums[i] != nums[i+1]:
        nums[count] = nums[i+1]
        count += 1
        
print(count)
print(nums)
```
- 只要找出来不一样的数字，然后把前面几个修改一下就可以，不用管后面的数据变成了什么，如果删除的话可以使用pop()，也可以使用index函数等

------
##### 最大子数组和动态规划


```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
# 方法一、暴力法n3
# 方法二、暴力法改n2
# 方法三、分治法nlogn
# 方法四、动态规划n
# 方法五、贪心n

# 穷举各种可能的「子数组和」
def fun1_baoli(nums):
	res = min(nums)
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			sum_num = 0
			for k in range(i, j+1): # 确定了一个范围
				sum_num += nums[k]
			res = max(res, sum_num)
	print(res)
# fun1_baoli(nums)


# 和方法一差不多，把确定的范围去掉了
def fun2_baoli_gaijian(nums):
	res = min(nums)
	for i in range(len(nums)):
		sum_num = 0
		for j in range(i, len(nums)):
			sum_num += nums[j]
			res = max(res, sum_num)
	print(res)

# fun2_baoli_gaijian(nums)



# f(i) = nums[0],i=0或f(i-1) <=0
# f(i) = f(i-1) + nums[i]， i 不等于 0并且f(i-1) > 0
def fun4_dontaiguihua(nums):
	nums_new = [0]*(len(nums)+1)
	res = min(nums)
	for i in range(1, len(nums)+1):
		nums_new[i] = max(nums_new[i-1], 0) + nums[i-1]
		res = max(res, nums_new[i])
	print(res)
# fun4_dontaiguihua(nums)

def fun5_tanxin(nums):
	sum_num = 0
	res = min(nums)
	for i in range(len(nums)):
		if sum_num < 0:
			sum_num = 0
		sum_num += nums[i]
		res = max(res, sum_num)
	print(res)
fun5_tanxin(nums)
```

------
