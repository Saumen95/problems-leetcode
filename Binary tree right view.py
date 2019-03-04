class Solution:
    # @param root, a tree node
    # @return a list of integers
    def levelorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.levelorder(root.left, level + 1, res)
            self.levelorder(root.right, level + 1, res)

    def rightSideView(self, root):
        res = []
        self.levelorder(root, 0, res)
        if res == []:
            return res
        val = []
        for elem in res:
            val.append(elem[-1])
        return val
