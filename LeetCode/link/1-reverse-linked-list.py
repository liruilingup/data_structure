class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class linkList(object):

    """初始化头结点"""
    def __init__(self, n):
        self.head = Node(None)

    """ 头插法建立链表 头结点->new新节点->节点"""
    def listCreateForward(self):
        if self.n == 0:
            return False
        else:
            temp = self.head
            for num in [1, 2, 3, 4]:
                node = Node(num)
                node.next = temp.next
                temp.next = node
                
        return new_head




def reverseList(head):
    """

    """
    new_head = None
    while head:
        # 为断开节点做一下准备
        tmp = head.next
        # 
        head.next = new_head
        new_head = head
        head = tmp
    return new_head



