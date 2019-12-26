class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        while head:
            nums += head.val,
            head = head.next
        def dfs(nums, l, r):
            if l > r:
                return 
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = dfs(nums, l, m-1)
            node.right = dfs(nums, m+1, r)
            return node
        return dfs(nums, 0, len(nums)-1)