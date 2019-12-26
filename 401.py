class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for i in range(1024):
            if bin(i).count('1') == num & i % 64 < 60 and i // 64 < 12:
                mn = str(i%64)
                if len(mn) < 2:
                    mn = '0' + mn
                
                hr = (i // 64)
                ans.append(str(hr) + ':' + mn)

        return ans