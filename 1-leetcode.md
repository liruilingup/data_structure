
### python编程常用
* ans = float('inf') 表示无穷大
* ans = float("-inf") 表示无穷小
* print(str(f).split('.')[0] + '.' + str(f).split('.')[1][:1]) # 保留一位小数，舍去方法
* abs(a - b) 表示绝对值
* max(a, b) 取最大的
* 指针可以使用start、end 或者 left、right
* 前后各去掉一位 s = s[1:-1]
* 转换成二进制，print(str(bin(255))), 前两位是0b
* Python lstrip() 方法用于截掉字符串左边的空格或指定字符。如：print(str('0123').lstrip('0'))

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
* 获取索引 nums = [1,2,3]，print(nums.index(2))


```python
temp = [x for x in range(0, 4)] # temp = [0, 1, 2, 3]
```
* 对10的9次方+7求余数 s = 3 % 1000000007

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

##### 判断是不是回文数字
```python
def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False


def isPalindrome(x):
    lst = list(str(x))
    while len(lst) > 1:
        if lst.pop(0) != lst.pop():
            return  False
    return True

def isPalindrome(x):
    lst = list(str(x))
    L, R = 0, len(lst)-1
    while L <= R:
        if lst[L] != lst[R]:
            return  False
        L += 1
        R -= 1
    return True
```



#### 最长回文子串
* 全部枚举
```python
s = 'cbbd'
# 纯暴力法，全部枚举
for i in range(len(s)-1):
    for j in range(len(s),i+1,-1):
        print(i,j, s[i:j])
```
* 动态规划

```python
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for x in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
```

* 使用枚举法，但是有优化条件

```python

# 做一个优化：
# 1、在第一个for循环之后，先判断已经求解的最大长度是否比接下来要比较的字符串长度要大，如果是大于待求解长度，则结束整个暴力求解，后面部分不需再求解
# 2、在第二个for循环中，长度不再是在从2开始增加，而是从最大长度开始

class Solution(object):
    def longestPalindrome(self, s):

        def ispalindrome(x): # 使用枚举法，但是有优化
            return x == x[::-1]
                
        #如果长度小于2或者本身就是回文串，返回s
        if len(s)<2 or s==s[::-1]:
            return s

        max_len = 1
        num = s[0]
        
        for i in range(len(s)-1):
            if max_len > len(s[i+1:]):           #待求解长度没有超过最大长度，结束
                break
            for j in range(i+max_len,len(s)):   #从长度为最大长度+1的子串开始求解
                # print(i, j, len(s), s[i:j+1])
                if ispalindrome(s[i:j+1]) and j-i+1>max_len:
                    max_len = j-i+1
                    num = s[i:j+1]
        return num

s = 'lababacde'
print(Solution().longestPalindrome(s))
```
##### 无重复子串
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length
```


##### 整数反转

```python
class Solution:
    def reverse(self, x: int) -> int:
        
        a = str(x)
        c=''
        for i in range(len(a)):
            c = c+str(a[len(a)-i-1])
            if c[-1]=='-':
                c = '-'+c[:-1]
        c = int(c)
        if c>=-2**31 and c <= 2**31-1:
            return c
        else:
            return 0

```

##### 丑数

```python
# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 =0
    while n>1:
        u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        umin = min(u2, u3, u5)
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        n -= 1
        ugly.append(umin)
    return ugly[-1]
print(nthUglyNumber(10))
```

##### 快乐数字
```python
def isHappy(n):
    res_table = set()
    while 1:
        n = [int(i) ** 2 for i in str(n)]
        n = sum(n)
        if n == 1:
            return True
        elif n in res_table:
            return False
        else:
            res_table.add(n)
print(isHappy(19))

```

#### 缺失数字
```python
def missingNumber(nums):
    nums.sort()
    if nums == [0]:
        return 1
    elif nums == [1]:
        return 0
    else:

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
print(missingNumber([9,6,4,2,3,5,7,0,1]))
```
#### 完全平方数
```python
def numSquares(n):
    lst = [i*i for i in range(1,n) if i*i <= n]
    dp = [0 for i in range(n+1)]
    for num in range(1,n+1):
        min_num = num
        for j in [c for c in lst if c <= num]:
            if dp[num-j] + 1 < min_num:
                min_num = dp[num-j] + 1
        dp[num] = min_num
    return dp[n]

print(numSquares(13))
```


##### 判断一个字符串是不是回文串

```python
s = 'abaoooo'
len_s = len(s)
pal_length = 1
for i in range(len_s, 0, -1):
    sub_string = s[0:i]
    if sub_string == sub_string[::-1]:
        pal_length = len(sub_string)
        break
print(pal_length)

``` 


#### 动态规划，完全平方数

* 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

```python
from typing import List
def numSquares(n: int) -> int:
    #完全背包 求装满背包所需要的最少重物
    coins= [i*i for i in range(1,n+1) if i*i <= n]
    #重物的列表
    dp=[float('inf')]*(n +1)

    dp[0]=0 #初始化不用任何重物填充容量为0的背包需要0个重物 填充容量为w>0不可行 设为float('inf)
    for i in coins:
        for j in range(i, n+1):
            dp[j]=min(dp[j],dp[j-i]+1)
    return dp[-1]

print(numSquares(1))

```

##### 平方数之和
* 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c**0.5)
        while i <= j:
            if i*i + j*j == c:
                return True
            elif i*i + j*j > c:
                j -= 1
            else:
                i += 1
        return False

```

## 字符串
#### 最长不含重复字符的子字符串

```python
s = "abcaaa"
queue = []

max_len = 0
for i in s:
    if i not in queue:
        queue.append(i)
    else:
        while queue[0] != i:
            queue.pop(0)
        queue.pop(0)
        queue.append(i)
    print(queue)
    max_len = max(max_len, len(queue))

print(max_len)
```

#### 数字反转
```python
class Solution:
    def reverse(self, x: int) -> int:
        #将整数的绝对值转换成字符串
        s=str(abs(x))
        #翻转字符串
        s=s[::-1]
        #如果输入整数是负数，增加负号
        if x <0:
            s ='-' + s
        #转换为整数
        result = int(s)
        #判断是否溢出
        if result>=-2**31 and result<=2**31-1:
            return result
        else:
            return 0

```


##### 丑数
* 丑数的递推性质： 丑数只包含因子 2, 3, 5 ，因此有 “丑数 == 某较小丑数 * 某因子” （例如：10 = 5 * 2）

```python
def nthUglyNumber(n: int) -> int:
    ## 利用数组记录
    dp, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2: a += 1
        if dp[i] == n3: b += 1
        if dp[i] == n5: c += 1
    return dp[-1]

print(nthUglyNumber(12))



```


##### 翻转数位
* 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

```python
class Solution:
    def reverseBits(self, num: int) -> int:
        pre, insert, m = 0,0,0
        for x in bin(num): #如果全是1，0b的第一个0也要算上
            print(x)
            if x == '1':
                pre += 1
                insert += 1
                m = max(m, insert)
            elif x == '0':
                insert = pre + 1
                pre = 0
                m = max(m,insert)
        return m

```


##### 移掉K位数字
* 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
* 两个相同位数的数字大小关系取决于第一个不同的数的大小。

```python
# https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
# "10200", 1
# "10", 1
# "10" 2

class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'
        # res = ''.join(stack[:remain]).lstrip('0')
        # return res if res else '0'
print(Solution().removeKdigits(num = "432219", k = 3))
```
#####  盛水的最大容器
* 使用双指针，移动短板
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) -1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, (j-i) * height[i])
                i += 1
            else:
                res = max(res, (j-i) * height[j])
                j -= 1
        return res
```



#####  最长公共前缀
* 输入: ["flower","flow","flight"]
* 输出: "fl"
```python

def fun():
    strs = ["flower","flow","flight"]

    length, count = len(strs[0]), len(strs)

    for i in range(length):
        c = strs[0][i]
        for j in range(1, count):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
    return strs[0]
print(fun()) 
```



-------


