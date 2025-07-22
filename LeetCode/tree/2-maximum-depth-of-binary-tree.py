def maxDepth(root):
    if not root:
        return 0
    else:
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
