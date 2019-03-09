"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        q = collections.deque()
        clones = {}
        clones[node] = Node(node.val, [])
        q.append(node)
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val, [])
                    q.append(nei)
                clones[curr].neighbors.append(clones[nei])
        return clones[node]
