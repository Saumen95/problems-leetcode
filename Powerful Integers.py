class Solution:
    def powerfulIntegers(self, x: 'int', y: 'int', bound: 'int') -> 'List[int]':
        a = []
        for i in range(100):
            for e in range(100):
                num = (x**i) + (y**e)
                if num <= bound:
                    a.append(num)
                else:
                    break
        return list(set(a))