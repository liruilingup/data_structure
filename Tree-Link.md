# 二叉树
[1.二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)  
[2.二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)  
[3.二叉树的后续遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)  
[4.二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)  

# 链表
[1.反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)  
[2.删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)  
[3.移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements/)  
[4.移除链表重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)  
[5.环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)  
* 给定一个链表，判断链表中是否有环。
使用快慢指针
```python
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
[6.环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)  
* 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
快慢指针之间走的步数有关系
```python
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
[7.排序链表](https://leetcode-cn.com/problems/sort-list/)  
[8.相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)  
