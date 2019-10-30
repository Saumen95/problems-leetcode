#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (59.79%)
# Likes:    803
# Dislikes: 92
# Total Accepted:    61.3K
# Total Submissions: 102.5K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        stack = [("",0)]
        while stack:
            curPath,ind = stack.pop()
            if len(curPath) == len(S):
                res.append(curPath)
            for i in range(ind,len(S)):
                if S[i].isdigit():
                    stack.append((curPath+S[i],i+1))
                else:
                    stack.append((curPath+S[i].lower(),i+1))
                    stack.append((curPath+S[i].upper(),i+1))
        return res
# @lc code=end

