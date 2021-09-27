import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        maxHeap = []
        coloumn = len(matrix[0])
        for r in range(row):
            for c in range(coloumn):
                heapq.heappush(maxHeap, -matrix[r][c])
                if(len(maxHeap) > k):
                    heapq.heappop(maxHeap)

        return - heapq.heappop(maxHeap)
