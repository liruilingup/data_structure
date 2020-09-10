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
