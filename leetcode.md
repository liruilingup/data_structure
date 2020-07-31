
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


### 排序的分类
* 插入排序：直接插入排序  希尔排序
* 交换排序：冒泡排序  快速排序
* 选择排序：简单选择排序  堆排序
* 归并排序


#####  直接插入排序

* 对于给定的一组记录，初始时假定第一个记录自成一个有序的序列，其余的记录为无序序列；接着从第二个记录开始，按照记录的大小依次将当前处理的记录插入到其之前的有序序列中，直至最后一个记录插入到有序序列为止。

```python
nums = [5, 2, 45, 6, 8, 2, 1]
def DirectInsertionSort(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            index, temp = i, nums[i]
            while index > 0 and nums[index-1] > temp:
                nums[index] = nums[index - 1]
                index -= 1
            nums[index] = temp

    print(nums)  
DirectInsertionSort(nums)


```




#####  希尔排序
* 改进插入排序
* 希尔排序也称为“缩小增量排序”，基本原理是：首先将待排序的元素分为多个子序列，使得每个子序的元素个数相对较少，对各个子序分别进行直接插入排序，待整个待排序序列“基本有序后”，再对所有元素进行一次直接插入排序。

```python
nums = [3, 12, 20, 2, 16, 14, 14, 11, 7, 14]
def ShellSort(nums):
    n = len(nums)
    gap = n // 2 # 步长
    while gap>= 1:
        for i in range(gap, n, 1): #可以设定步长
            j = i
            temp = nums[j]
            while j>=gap and nums[j-gap] >= temp: #该位置的数比temp大就往后移
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp
        gap = gap // 2  # 控制间隙的变化
ShellSort(nums)
print(nums)

```

#####  冒泡排序
* 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
```python
nums = [5,2,45,6,8,2,1]
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
bubble_sort(nums)

```




##### 快速排序（高效）
* 采用“分而治之”的思想，把大的拆分为小的，小的在拆分为更小的。
* 原理：对于一组给定的记录，通过一趟排序后，将原序列分为两部分，其中前部分的所有记录均比后部分的所有记录小，然后再依次对前后两部分的记录进行快速排序，递归该过程，直到序列中的所有记录均为有序为止。

```python
# 通过比较大小进行移动，然后使用递归，注意myList[i] = base
def QuickSort(myList, start, end):
    if start < end:
        i, j = start, end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j -= 1    
            myList[i] = myList[j]
            while (i < j) and (myList[i] <= base):
                i += 1
            myList[j] = myList[i]
        myList[i] = base
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


myList = [7, 6, 5, 3, 12, 20, 1, 9, 11, 4, 15, 10, 8]
print("myList:",QuickSort(myList, 0, len(myList) - 1))

```



##### 简单选择排序
* 从无序数列中选取最小的元素和无序数列中的第一个元素交换，每轮都可以确定最小元素的位置。直到选到一个最小的数，将它放在第一位
* 对于给定的一组记录，经过第一轮比较后得到最小的记录，然后将记录与第一个记录的位置进行交换；接着对不包括第一个记录以外的其他记录进行第二轮排序，得到最小的记录并与第二个记录进行位置交换；重复该过程，直到进行比较的记录只有一个为止。

```python
def simpleSelectSort(series):
    for i in range(len(series)):
        for j in range(i+1,len(series)):
            if series[j] < series[i]:
                series[j],series[i] = series[i],series[j]

data = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 1,16]
simpleSelectSort(data)
print(data)
```



##### 归并排序
* 先分开再合并，分开成单个元素，合并的时候按照正确顺序合并（分成两个函数，一个拆分数组，一个合并数组）
* 利用递归与分治技术将数据序列划分为越来越小的半子表，再对半子表排序，最后再用递归步骤将排好序的半子表合并成为越来越大的有序序列。
* 原理：对于给定的一组记录，首先将两个相邻的长度为1的子序列进行归并，得到n/2个长度为2或者1的有序子序列，在将其两两归并，反复执行此过程，直到得到一个有序的序列为止。

```python
def merge_sort(li):
    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li
    #取拆分的中间位置
    mid = len(li) // 2  #取整除
    #拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]

    #对拆分过后的左右再拆分 一直到只有一个元素为止
    #最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort(left)
    rl =merge_sort(right)

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll , rl)

#这里接收两个列表
def merge(left , right ):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left)>0 and len(right)>0 :
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0)) # left.pop(0)是列表的第一个数字
        else:
            result.append(right.pop(0))
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result

if __name__ == '__main__':
    nums = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0, 1,16]
    li2 = merge_sort(nums)
    print(li2)

```


------

### 查找

##### 二分查找
* 二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。

```python
def binary_search(nums,item):
    """二分查找"""
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid_index = (low+high)//2
        if nums[mid_index] == item:
            return "找到元素! 在原列表索引为{0}的位置".format(mid_index)
 
        elif nums[mid_index]<item:
            low = mid_index+1
        else:
            high = mid_index-1
    return "未能找到"
 
if __name__ == '__main__':
    nums = [1,3,4,9,10,15,17,34]
    result_index1 = binary_search(nums,9)
    result_index2 = binary_search(nums,2)
    print("能否查找到 9：",result_index1)
    print("能否查找到 2：",result_index2)
```

------





