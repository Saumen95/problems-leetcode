class Solution:
    # @param root, a tree node
    # @return a boolean
    def sym(self, left, right):
        if left == None and right == None:  # null tree is symmetric by definition
            return True
        if left and right and left.val == right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.sym(root.left, root.right)
