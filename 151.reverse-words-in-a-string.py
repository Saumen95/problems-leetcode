#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        sl=s.split()
        return ' '.join(reversed(sl))

        
# @lc code=end

