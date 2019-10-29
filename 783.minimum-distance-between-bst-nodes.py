#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (51.07%)
# Likes:    435
# Dislikes: 127
# Total Accepted:    43K
# Total Submissions: 84.1K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def min_node(self, root, array):
        if root is None:
            return

        self.min_node(root.left, array)
        array.append(root.val)
        self.min_node(root.right, array)


    def minDiffInBST(self, root: TreeNode) -> int:
        array = []
        self.min_node(root, array)
        size = len(array)
        min_diff = sys.maxsize
        for i in range(1, size):
            min_diff = min(min_diff, array[i] - array[i - 1])

        if min_diff == sys.maxsize:
            return 0
            
        else:
            return min_diff   
        
# @lc code=end

