"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            for i in range(2 ** level - 1):
                node = queue.popleft()
                nextnode = queue[0]
                node.next = nextnode
                if node.next is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            node = queue.popleft()
            node.next = None
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

            level += 1
        return root
