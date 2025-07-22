class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = []
    if root:
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)
    return res