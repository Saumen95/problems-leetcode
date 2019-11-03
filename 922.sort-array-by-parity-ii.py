#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            while A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j += 2
        return A
# @lc code=end

