class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pointer = None

        def traverse(root):
            if not root:
                return
            traverse(root.right)
            traverse(root.left)
            root.right = self.pointer
            root.left = None
            self.pointer = root
        traverse(root)
