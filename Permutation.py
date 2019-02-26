
class Solution:
    def permute(self, nums):
        res = []

        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
        dfs(nums, [], res)
        return res

    def permute1(self, nums):
        res = []

        def dfs(nums=nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        dfs()
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.permute(nums=[1, 2, 3]))
