class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        self.m_ways = {}
        self.m_ways[""] = 1

        def ways(s):
            if s in self.m_ways:
                return self.m_ways[s]
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            w = ways(s[1:])
            prefix = int(s[:2])
            if prefix <= 26:
                w += ways(s[2:])
            self.m_ways[s] = w
            return w
        return ways(s)
