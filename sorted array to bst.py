# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  complexity O(n)


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # the order of inserting matters=> balance or not

        def BSTinsertBalanced(root, nums):
            if nums == []:
                return None
            else:
                # easy to forget to initialize
                root = TreeNode(nums[len(nums) / 2])
                root.left = BSTinsertBalanced(root.left, nums[:len(nums) / 2])
                root.right = BSTinsertBalanced(
                    root.right, nums[len(nums) / 2 + 1:])
                return root
        newRoot = TreeNode(0)
        return BSTinsertBalanced(newRoot, nums)
