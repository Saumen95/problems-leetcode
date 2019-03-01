class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        que = [root]
        while que:
            ans.append(1.0 * sum([n.val for n in que]) / len(que))
            nque = []
            for n in que:
                if n.left:
                    nque.append(n.left)
                if n.right:
                    nque.append(n.right)
            que = nque
        return ans
