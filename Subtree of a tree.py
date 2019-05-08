# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def serialize(node):
            if not node:
                return '#'
            return serialize(node.left) + str(node.val) + serialize(node.right)
        serialized_t = serialize(t)
        exists = [False]
        def traverse(node):
            if not node:
                return '#'
            serialized_tree = traverse(node.left) + str(node.val) + traverse(node.right)
            if serialized_tree == serialized_t:
                exists[0] = True
            return serialized_tree
        traverse(s)
        return exists[0]