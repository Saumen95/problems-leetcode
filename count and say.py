class Solution:

    def doCountAndSay(self, src):
        char = src[0]
        num = 0
        result = ""
        for c in src:
            if char == c:
                num += 1
            else:
                result += (str(num) + char)
                char = c
                num = 1
        result += (str(num) + char)
        return result

    # @return a string
    def countAndSay(self, n):
        if 0 == n:
            return ""
        elif 1 == n:
            return "1"
        result = "1"         # str is a keyword
        for i in range(1, n):
            result = self.doCountAndSay(result)
        return result
