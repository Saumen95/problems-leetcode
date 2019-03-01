
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, solution, level):
        if root:
            if len(solution) < level + 1:
                solution.append([])
            solution[level].append(root.val)
            if root.left:
                self.preorder(root.left, solution, level + 1)
            if root.right:
                self.preorder(root.right, solution, level + 1)

    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        solution = []
        self.preorder(root, solution, 0)
        for index in range(len(solution)):
            if index % 2 == 1:
                solution[index].reverse()
        return solution
