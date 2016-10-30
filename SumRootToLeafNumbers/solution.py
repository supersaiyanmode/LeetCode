# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.total(root)
    
    def total(self, root, paths=None):
        if paths is None: paths = []
        if not root.left and not root.right:
            return int("".join(map(str, paths + [root.val])))
        result = 0
        if root.left:
            result += self.total(root.left, paths + [root.val])
        if root.right:
            result += self.total(root.right, paths + [root.val])
        return result
            
            
        