
class Solution(object):
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
      def invert(root):
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
          invert(root.left)
        if root.right:
          invert(root.right)
      invert(root)
    return root
