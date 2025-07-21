# 数组
## 1、最长连续序列， 
1.先排序，
2.然后再计算差是不是 1
## 2、和为 K 的子数组 (子串)，计算个数 
1.暴力破解
2.前缀和的方法
## 3、最大子数组和 (普通数组)   
1.使用动态规划的解法
 
# 移动数组
## 1、移动零
j = 0
for k in nums:
    if k != 0:
        nums[j] = k
        j += 1
for m in range(j ,len(nums)):
    nums[m] = 0
## 2、轮转数组

nums.insert(0, nums.pop())


思维活跃的时候，就拓展新的解题方法；
烦躁的时候，就总结经验
刷题记录：
周一  周二  周三  周四  周五  周六  周日
                        
                        
3.24
复习刷题                        
3.17
复习贪心-字母划分 (本质是区间合并)                     
                    3.15
学习贪心算法  3.16
学习贪心算法



1.哈希：3道题
2.双指针：3/4 道题
3.滑动窗口：2道题
4.子串：1/3道题
5.普通数组：4/5道题
6.矩阵：4道题
7.链表：2/14道题
8.二叉树：5/15道题
9.图论：放弃
10.回溯：3/8  道题
11.二分查找：2/6 道题
12.栈：3/5 道题
13.堆： 2/3 道题
14.贪心：1/4 道题
15.动态规划：3/10 道题
16.多维动态规划：2/5 道题
17.技巧：5 道题

第二遍刷题

常规（哈希、双指针）  2-3天        
链表+二叉树  1天      
堆和栈、回溯  1天      
贪心和动态规划 1天      
二分查找和排序 1天      

1.哈希：3道题
1、两数之和：
hash记录k，v enumerate(nums)
res = {}
for k,v in enumerate(nums):
if target-v in res:
return [k, res[target-v]]
else:
res[v] = k


2、字母异位词分组：
对每一个单词先排序， 再join 组合到一起，一样的都是一个排序好的key，value记录一样的单词
res_dict = {}
for str in strs:
tmp = "".join(sorted(list(str)))
if tmp in res_dict:
res_dict[tmp].append(str)
else:
res_dict[tmp] = [str]
res = []
for key, value in res_dict.items():
res.append(value)
return res


3、最长连续序列：
不会使用hash，可以先排列，然后判断i，i+1的数组是不是相差1
nums.sort()
tmp = 1
res = 1
for i in range(1, len(nums)):
if nums[i-1] + 1 == nums[i]:
tmp += 1
res = max(res, tmp)
elif nums[i-1] == nums[i]:
continue
else:
tmp = 1
2.双指针：3/4 道题
4、移动零
不是0的直接插入数组里面，然后记录0的个数最后直接赋值
if not nums: return 0
j = 0
for i in range(len(nums)):
if nums[i]:
nums[j] = nums[i]
j += 1
for k in range(j, len(nums)):
nums[k] = 0


5、盛最多水的容器
i和j：谁小，就谁先移动一下
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


6、三数之和
记得先排序一下：while里面判断，然后移动i和j，因为有可能相等的情况，很多次while判断

3.滑动窗口 2道题
7、无重复字符的最长子串
不要跟重复的子串搞混了，判断子数组的len和子数组set的len
strs_list = list(s)
tmp = 1
for i in range(len(strs_list)-1):
j = i + 1
# tmp_str = [strs_list[i]]
while j <= len(strs_list)-1:
if len(strs_list[i:j+1]) == len(set(strs_list[i:j+1])):
j += 1
tmp = max(tmp, j - i)
else:
tmp = max(tmp, j - i)
break



8、找到字符串中所有字母异位词
判断子串排序之后的join字符串是不是一样
p_sorted = "".join(sorted(list(p)))

res = []
strs = list(s)
for i in range(len(strs) - p_len+1):
tmp = "".join(sorted(strs[i:i + p_len]))
if tmp == p_sorted:
res.append(i)

10、最大子数组和
使用动态规划 dp[i] = max(dp[i-1], dp[i-1] + num[i])
dp = [0] * len(nums)
dp[0] = nums[0]
for i in range(1, len(nums)):
dp[i] = max(dp[i-1] + nums[i], nums[i])


11、合并区间
记得先排序，然后只需要判断右边的数字即可
intervals_sorted = sorted(intervals, key=lambda x:x[0])
ans = []
for p in intervals_sorted:
if ans and p[0] <= ans[-1][1]: # 可以合并
ans[-1][1] = max(ans[-1][1], p[1]) # 更新右端点最大值
else: # 不相交，无法合并
ans.append(p) # 新的合并区间


12、轮转数组
可以先pop然后insert（0， nums.pop（））
for _ in range(k):
nums.insert(0, nums.pop())

13、除自身以外数组的乘积
暴力会超时、模拟成二维码矩阵，算上三角和下三角

4.矩阵
14、矩阵置零
先找出来0的坐标， 两个for循环
然后行和列进行赋值0

15、螺旋矩阵
while里面判断，left、right、top、bottom之间的变化关系

16、旋转图像
坐标之间的关系记录，matrix[j][n - 1 - i] = tmp[i][j]


17、搜索二维矩阵 II
读取一遍行，然后判断一行里面的最大值和最小值即可

5.链表
18、相交链表 (核心就是head = head.next)
只要A和B不想等，就A=A.next \ B=B.next 
核心在于 A 链表 + B 链表，与 B 链表 + A 链表必然是相同的长度，所以一定会同时遍历到结尾
A , B = headA, headB
while A != B:
A = A.next if A else headB
B = B.next if B else headA
return A

19、链表反转
3个节点的4次交换
new_head = None
while head:
# 为断开节点做一下准备
tmp = head.next
# 
head.next = new_head
new_head = head
head = tmp
return new_head

20、回文链表
双指针（快慢指针），有点难
方法2：一遍遍历，然后使用 nums == nums[::-1]判断

 21、环形链表
遍历一遍节点，使用集合判断是否有重复的

22、合并两个有序的链表
1.记得有个当前节点记录节点
2.记得最后合并链表剩余的部分：cur.next = list1 if list1 else list2

6.树
23 二叉树的最大深度
判断 max(depth(left), depth(root.right)) + 1
if not root:
return 0
else:
return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1


24 中序遍历二叉树
左根右
res = []
if root:
   self.order(root.left)
   res.append(root.val)
   self.order(left.right)
return res
25 翻转二叉树
if not root: return
tmp = root.left
root.left = self.invertTree(root.right)
root.right = self.invertTree(tmp)
return root

26 对称二叉树
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
def recur(L, R):
if not L and not R: return True
if not L or not R or L.val != R.val: return False
return recur(L.left, R.right) and recur(L.right, R.left)
return not root or recur(root.left, root.right)


27 平衡二叉树
def isBalanced(self, root: Optional[TreeNode]) -> bool:
if root is None:return True
return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

def height(self, root: Optional[TreeNode]) -> bool:
if root is None:return 0
return max(self.height(root.left), self.height(root.right)) + 1
28 二叉树的层序遍历
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
if root is None:
return []
ans = []
cur = [root]
while cur:
nxt = []
vals = []
for node in cur:
vals.append(node.val)
if node.left: nxt.append(node.left)
if node.right: nxt.append(node.right)
cur = nxt
ans.append(vals)
return ans

29 全排列
def permute(self, nums: List[int]) -> List[List[int]]:
def dfs(x):
if x == len(nums) - 1:
res.append(list(nums)) # 添加排列方案
return
for i in range(x, len(nums)):
nums[i], nums[x] = nums[x], nums[i] # 交换，将 nums[i] 固定在第 x 位
dfs(x + 1) # 开启固定第 x + 1 位元素
nums[i], nums[x] = nums[x], nums[i] # 恢复交换
res = []
dfs(0)
return res
30 子集
def subsets(self, nums: List[int]) -> List[List[int]]:
res = []
tmp = []
n = len(nums)
def dfs(i):
res.append(tmp[:])
for k in range(i, n):
tmp.append(nums[k])
dfs(k+1)
tmp.pop()
dfs(0)
return res
全排列和子集的区别：
1.全排列是len(tmp) == len(nums) for i in nums
2.子集是 for k in range(i, n)

31 堆-数组中的第K个最大元素




18.动态规划：3/10 道题

31 爬楼梯
n个台阶，一个1个或者2个，有多少种方法
方法1: 递归
if n<=2:return n
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(2, n):
dp[i] = dp[i-1] + dp[i-2]
return dp[-1]


方法2: 动态规划 (会超时)
def dfs(i):
if i == 1 or i == 2:
return i
else:
return dfs(i-1) + dfs(i-2)
return dfs(n)

32 杨辉三角
核心思想就是计算

def generate(n):
    res=[[1], [1,1]]
    def dfs(i):
        # 3
        tmp = [1]
        for j in range(1, i-1):
            tmp.append(res[-1][j-1] + res[-1][j])
        tmp.append(1)

        res.append(tmp)

    for k in range(3, n+1):
        dfs(k)

    print(res)


generate(5)


32 打家劫舍
核心思想就是：dp[i-1], dp[i-2], 有可能跳过两个然后去偷第三家的情况
dp[i] = max(dp[i-2]+nums[i], dp[i-1])

33 最少的硬币--是背包问题，是有dp算法
核心思想就是 dp[i] = min(dp[i], dp[i-各个硬币])
for i in amount:
for coin in coins:
dp[i] = min(dp[i], dp[i-coin])
19.贪心算法：3/10 道题
34 买卖股票的时机--是贪心算法
核心思想就是：min 和 max的判断; 记录的局部最低，不是全局最低
profix = "-1"
low = "inf"
for i in nums:
low = min(low, i)
profix = max(profix, )

35 跳跃游戏--是贪心算法
最远能到达某个位置，就一定能到达它前面的任何位置。核心是判断k+v的值，索引和值的关系
nums = []
max_jump = 0
for i, v in nums:
    if max_jump>=k and k+v>max_jump:
        max_jump = k+v
if max_jump>len(nums)-1: print True


35 跳跃游戏2--是贪心算法
求取跳跃的最小次数
我们遍历 [0,..n−2] 的每一个位置 i，对于每一个位置 i，我们可以通过 i+nums[i] 计算出当前位置能够到达的最远位置，
我们用 mx 来记录这个最远位置，即 mx=max(mx,i+nums[i])。
接下来，判断当前位置是否到达了上一次跳跃的边界，即 i=last，如果到达了，那么我们就需要进行一次跳跃，将 last 更新为 mx，
并且将跳跃次数 ans 增加 1。

jump = mx = last = 0
for i, x in enumerate(nums[:-1]):
mx = max(mx, i + x)
if last == i:
jump += 1
last = mx
return jump 


36 划分字母区间--是贪心算法、本质是合并区间
1.划分为尽可能多的片段
2.同一字母最多出现在一个片段中

3.15、3.16、3.17 三天学习了贪心算法



刷题第二遍
2025.7.20
和为 k 的子数组和，跟两数之和是一个道理
https://leetcode.cn/problems/subarray-sum-equals-k/solutions/2781031/qian-zhui-he-ha-xi-biao-cong-liang-ci-bi-4mwr/?envType=study-plan-v2&envId=top-100-liked

前缀和的定义：s[0]=0, s[i+1]=nums[0]+nums[1]+⋯+nums[i]。
设 i<j，如果 nums[i] 到 nums[j−1] 的元素和等于 k，用前缀和表示，就是
s[j]−s[i]=k
眼熟吗？写成 s[j]+(−s[i])=k 就能看得更明白

最长连续序列， 1.先排序，
2.然后再计算差是不是 1
和为 K 的子数组 (子串)，计算个数 1.暴力破解
2.前缀和的方法
最大子数组和 (普通数组)   3.使用动态规划的解法
    



移动零 j = 0
    for k in nums:
        if k != 0:
            nums[j] = k
            j += 1
    for m in range(j ,len(nums)):
        nums[m] = 0

轮转数组    4.nums.insert(0, nums.pop())
    5.使用动态规划的解法
    


子串

普通数组




