
def levelOrder(root):
    if root is None:
        return []
    ans = []
    cur = [root]
    while cur:
        nxt = []
        vals = []
        for node in cur:
            vals.append(node.val)
            if node.left:  nxt.append(node.left)
            if node.right: nxt.append(node.right)
        cur = nxt
        ans.append(vals)
    return ans
