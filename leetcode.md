
### python编程常用
* ans = float('inf') 表示无穷大
* ans = float("-inf") 表示无穷小
* abs(a - b) 表示绝对值
* max(a, b) 取最大的
* 指针可以使用start、end 或者 left、right


------

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

#### 重新排列字符串 

* 请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

```python
# 方法一
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print("".join([i[1] for i in sorted([(indices[i], s[i]) for i in range(len(s))])]))

# 方法二，res先得到indices的数字然后存储字符
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = ["" for i in range(len(s))]
print(res)
for i in range(len(s)):
	res[indices[i]] = s[i]
print("".join(res))

```

------


#### 两个数组的交集 II

```python
# 方法一双指针

# 对数组进行排序
# [1,1,2,2]
# left 和right进行比较
# [2,2]
# right

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1.sort()
nums2.sort()
r = []
left, right = 0, 0
while left < len(nums1) and right < len(nums2):
	if nums1[left] < nums2[right]:
		left += 1
	elif nums1[left] == nums2[right]:
		r.append(nums1[left])
		left += 1
		right += 1    
	else:
		right += 1
print(r)

# 方法二，判断然后移除

nums1 = [1,2,2,1]
nums2 = [2,2]

a = 0
res = []
if len(nums1) > len(nums2):
	nums1, nums2 = nums2, nums1
while a < len(nums1):
	if nums1[a] in nums2:
		res.append(nums1[a])
		nums2.remove(nums1[a])
	a += 1

print(res)


```


------

#### 等差数列 

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if arr[0] == arr[-1]:
            return True
        if len(arr) == 0 or len(arr) == 1:
            return True
            
        chazhi = arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != chazhi:
                return False
        return True
```


------
#### 三数之和
* 三个数相加和是0
* 先排序，使用双指针，相同的时候要注意next
```python
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
print(nums)
sum_num = 0
res = []
for i in range(len(nums)-2):
	if nums[i] >0:
		break
	if(i>0 and nums[i]==nums[i-1]): # 重复的就next
		continue
	left,right = i+1, len(nums)-1
	while left < right:
		s = nums[i] + nums[left] + nums[right]
		if s < 0:
			left += 1
			while left < right and nums[left] == nums[left - 1]: left += 1  # 重复的就next
		elif s >0:
			right -= 1
			while left < right and nums[left] == nums[left - 1]: right -= 1 # 重复的就next
		else:
			res.append([nums[i], nums[left], nums[right]])
			left += 1
			right -= 1
			while left < right and nums[left] == nums[left - 1]: left += 1 # 重复的就next
			while left < right and nums[left] == nums[left - 1]: right -= 1 # 重复的就next

print(res)
```
------

#### 最接近的三数之和

```python
# 要比较差值ans和target和三数之和t的关系
# 根据target和t的关系，决定left和right的变化
def threeSumClosest():
	nums = [-1,2,1,-4]
	# nums = [1,1,1,0]
	nums = [0,2,1,-3]
	target = 1
	nums.sort()
	if not nums: return 0
	if len(nums) < 3: return sum(nums)
	ans = float('inf')
	for i in range(len(nums)):
		if i > 0 and nums[i] == nums[i-1]: continue

		left, right = i+1, len(nums)-1
		while left < right:
			t = nums[i] + nums[left] + nums[right]
			if t == target: return target
			if abs(target - t) < abs(target - ans): 
				ans = t
			if t < target:
				left += 1
			if t > target:
				right -= 1
	return ans
result = threeSumClosest()
print(result)
```

------


#### 四数之和

```python
# 注意相同的时候要next一下，否则会有影响，还有next的位置是在相同的时候
nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()
res = []

for i in range(len(nums)-3):
	if i > 0 and nums[i] == nums[i-1]:
		continue
	for j in range(i+1, len(nums)-2):
		if j > i+1 and nums[j] == nums[j-1]:
			continue
		start = j +1
		end = len(nums)-1
		while  start < end:
			s = nums[i]+nums[j]+nums[start]+nums[end]
			if s == target:
				res.append([nums[i], nums[j], nums[start], nums[end]])
				while start < end and nums[start] == nums[start+1]:
					start += 1
				while start < end and nums[end] == nums[end - 1]:
					end -= 1
				end -= 1
				start += 1
			elif s > target:
				end -= 1
			else:
				start += 1
print(res)

```

------

#### n个数全排列
* 这个问题可以看作有n个排列成一行的空格，我们需要从左往右依此填入题目给定的n个数，每个数只能使用一次。那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此尝试填入一个数，看能不能填完这n个空格，在程序中我们可以用「回溯法」来模拟这个过程

```python
# 方法一、使用类似dfs的递归

def get_full_resolution(store, temp_list, test_list):
    # 递归停止条件
    # temp_list用来存储一种完整的全排列
    # 如果长度已经和原始的输入test_list相等,则将这一种全排列存储下来
    # 继续找下一种全排列
    if len(temp_list) == len(test_list):
        store.append(temp_list[:])
    else:
        # 遍历原始输入中的元素,每次取出一个元素
        for i in test_list:
            if i in temp_list:
                continue
            # 如果当前遍历到的点不在temp_list中
            # 则添加到该列表中
            temp_list.append(i)
            # 添加完一个点之后,剩下的过程其实可以看成同样的过程
            get_full_resolution(store, temp_list, test_list)
            # 当找到一种全排列之后,就删掉一个点(往后退一步),继续判断其它的情况
            temp_list.pop()  #每次都是找到全排列的时候pop()一次，返回上一层，还会再pop()一次，就变成[1,2]

store=[]
temp_list=[]
test_list=[1,2,3]
get_full_resolution(store, temp_list, test_list)
print(store)
```

* 同方法一

```python
# 自己写的
class Solution:
    def permute(self, nums):   
        
        def dfs_pailie(tmp):
            if len(nums) == len(tmp):
                store.append(tmp[:])  #注意tmp[:]和tmp()的区别
            else:
                for i in nums:
                    if i in tmp:
                        continue
                    tmp.append(i)
                    dfs_pailie(tmp)
                    tmp.pop()
        
        store = []
        tmp = []
        dfs_pailie(tmp)
        return store
a = Solution().permute(nums = [1,2,3])
print(a)
```

------
