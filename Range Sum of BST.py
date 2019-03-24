# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.x= 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root.left:
            self.rangeSumBST(root.left, L, R)
        if L <= root.val <= R:
            self.x += root.val
            if root.val == R:
                return self.x
        if root.right:
            self.rangeSumBST(root.right, L, R)
        return self.x
