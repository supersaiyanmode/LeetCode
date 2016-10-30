# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.get_path(root, p)
        path_q = self.get_path(root, q)
        print [x.val for x in path_p]
        print [x.val for x in path_q]
        previous = root
        for p_p, q_p in zip(path_p, path_q):
            if p_p.val != q_p.val:
                return previous
            previous = p_p.val
        return previous
    
    def get_path(self, root, node):
        queue = [(root,[root])]
        while queue:
            front, path = queue.pop(0)
            if front == node:
                return path
            if front.left:
                queue.append((front.left, path + [front.left]))
            if front.right:
                queue.append((front.right, path + [front.right]))
        return None
                
        