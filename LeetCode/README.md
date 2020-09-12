# 目录

[环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)  
* 给定一个链表，判断链表中是否有环。
 
```python
# 使用快慢指针 
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False

        slow, fast = head, head
        while fast and fast.next: # while终止的条件
            slow = slow.next
            fast = fast.next.next
            if slow == fast:     # 判断快慢指针是否相同
                return True
        return False
```
[环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)  
* 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。  
```python
#快慢指针之间走的步数有关系 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None: return

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
```
[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)  

* 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。
* 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
* 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
* 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
* 输出：7 -> 0 -> 8
* 原因：342 + 465 = 807
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s :
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0) #先从个位相加，l1就是个位开始
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

[两数之和](https://leetcode-cn.com/problems/two-sum/)
* 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
* 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
```python
def twoNum(nums, target):
    hashMap = {}
    for index, num in enumerate(nums):
        hashMap[num] = index

    for i, num in enumerate(nums):
        j = hashMap.get(target-num)
        if j is not None and i!=j:
            return [i,j]
# 方法二
nums = [9, 9, 11, 15]
target = 18
def twoNum1(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums and (target - nums[i] != nums[i]): # 要考虑相等情况，并且数组中两个数一样
            return [i, nums.index(target - nums[i])]
        if (target - nums[i] == nums[i]) and nums.count(nums[i]) > 1:
            count = 0
            for k in range(len(nums)):
                if nums[k] == nums[i]:
                    count += 1
                if count == 2:
                    return [i, k]
    return []
print(twoNum1(nums, target))
```
[回文数](https://leetcode-cn.com/problems/palindrome-number/)
* 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
```
[三数之和](https://leetcode-cn.com/problems/3sum/)
* 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

```python
nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif s > 0:
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
    return res
print(threeSum(nums))

```
