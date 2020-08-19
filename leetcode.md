
### python编程常用
* ans = float('inf') 表示无穷大
* ans = float("-inf") 表示无穷小
* print(str(f).split('.')[0] + '.' + str(f).split('.')[1][:1]) # 保留一位小数，舍去方法
* abs(a - b) 表示绝对值
* max(a, b) 取最大的
* 指针可以使用start、end 或者 left、right
* python反转一个列表
```python
a=[1,2,3,4,5]
for i in a[::-1]:  #a列表不变
  print(i)
```
* python倒着循环
```python
for i in range(5, 0, -1):
    print(i)   # 结果是5，4，3，2，1
```

* readline()是读取一行，结果是一个str
* readline().split()，结果是一个列表
```python
list_num = sys.stdin.readline().split() # spilt() 是把结果放到一个列表中
N,M,K = [int(list_num[i]) for i in range(len(list_num))]
N,M,K = map(int, list_num)
res = list(map(int, list_num))
```
* 获取索引
* 对10的9次方+7求余数

```python
temp = [x for x in range(0, 4)] # temp = [0, 1, 2, 3]
# 获取索引
nums = [1,2,3]
print(nums.index(2))
```


##### python初始化函数
```python
# 初始化函数没有参数
class tree:
    def __init__(self):
        return
# 初始化函数有参数
class tree:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
```
##### python打印不换行
```python
for i in range(4):
	print(i, end = ' ')
```

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



### 排列、组合、子集

##### 组合，1-n里面选取k个数组合
* 方式一
```python
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()
a = Solution().combine(4,3)
print(a)
```
* 方式二，同方法一但是又一种写法

```python
def dfs(start, k,n,tmp,res):
    if len(tmp) == k:
        res.append(tmp[:])
    else:
        for i in range(start, n+1): #4的时候，for没有运行，返回，又pop()所以没有[4]
            tmp.append(i)
            dfs(i+1, k,n,tmp,res)
            tmp.pop()
res = []
tmp = []
dfs(1,2,4,tmp,res)
print(res)
```


##### 组合总数
* 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

```python
# nonlocal
# 第一，两者的功能不同。global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
# 第二，两者使用的范围不同。global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，并且外层函数中定义了相应的局部变量，否则会发生错误

candidates = [3,2,6,7] 
target = 7
res = []
tmp_list = []
def zuhe(tmp, tmp_list):
    if tmp == target:
        res.append(tmp_list[:])
    if tmp > target:
        return
    for i in candidates: 
        if tmp_list and  tmp_list[-1] > i: #防止重复的
            continue
        zuhe(tmp+i, tmp_list+[i])
zuhe(0, [])
print(res)
```


##### 组合总数2
* 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
```python
candidates = [2,5,2,1,2]
target = 5
result = []
candidates.sort()
# [1, 1, 2, 5, 6, 7, 10]

print('-----------',candidates)
def zuhe2(tmp, tmp_list, nums):
    print(nums)
    if tmp == target :
        result.append(tmp_list[:])
    if tmp > target:
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:  #相同时需要剪枝
            continue
        tmp_list.append(nums[i])
        zuhe2(tmp + nums[i], tmp_list, nums[i+1:]) #递归返回的数组
        tmp_list.pop()

zuhe2(0, [], candidates)
print(result)


```


##### 子集，同m个数组中选取n个进行排列
* 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
```python
nums = [1,2,3,4,5]
res = []
res.append([])
res.append(nums)
for k in nums:
    res.append([k])
print(res)
# 选一些数字进行排列

def zuhe_n(nums, tmp, n):
    if len(tmp) == n:
        res.append(tmp[:])
    else:
        for i in range(len(nums)):
            tmp.append(nums[i])
            zuhe_n(nums[i+1:], tmp,n)  #递归的条件
            tmp.pop()
    return res

for i in range(2, len(nums)):
    a = zuhe_n(nums, [], i)
print(res)
```



##### 子集2，数组有重复的
* https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-suan-fa-by-powcai-6/
* 方法一、同子集1一样，但是去掉重复的列表，nums需要排序
```python


nums = [1,2,2]
nums.sort()
res = []
res.append([])
res.append(nums)
for k in nums:
    if [k] not in res:
        res.append([k])
print(res)

def zuhe_n(nums, tmp, n):
    if len(tmp) == n and tmp[:] not in res:
        res.append(tmp[:])
    else:
        for i in range(len(nums)):
            tmp.append(nums[i])
            zuhe_n(nums[i+1:], tmp,n)  #递归的条件
            tmp.pop()
    return res

for i in range(2, len(nums)):
    a = zuhe_n(nums, [], i)
print(res)
```



* 方法二、递归

```python

nums = [1,2,4,4,4,4,4,4]
res = []
n = len(nums)

nums.sort()
def helper(idx, tmp):
    res.append(tmp)
    for i in range(idx, n):
        if i > idx and nums[i] == nums[i-1]:
            continue
        helper(i + 1, tmp + [nums[i]])

helper(0, [])
print(res)


```


* 方法三、迭代
```python
nums = [1,2,4,4,4,4,4,4]

res = [[]]
cur = []

for i in range(len(nums)):
    print(res)
    if i > 0 and nums[i-1] == nums[i]:
        cur = [tmp + [nums[i]] for tmp in cur]
    else:
        cur = [tmp + [nums[i]] for tmp in res]

    res += cur

print(res)


```

##### 买卖股票1
* 交易一次
```python
# 画出折线图，落差最大的就是
prices = [7,1,5,3,6,4]
minprice = float('inf')
maxprofit = 0
for price in prices:
    minprice = min(minprice, price)
    maxprofit = max(maxprofit, price - minprice)
print(maxprofit)
```

##### 买卖股票2
* 交易多次
```python
# 使用贪心，只要第二天大于第一天的卖掉
prices = [7,1,5,3,6,4]
profit = 0
for i in range(1, len(prices)):
    tmp = prices[i] - prices[i - 1]
    if tmp > 0:
        profit += tmp
print(profit)
```


-------


