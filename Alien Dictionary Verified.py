class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        m = {char: i for i, char in enumerate(order)}

        for i in range(1,len(words)):
            
            last_word = words[i-1]
            this_word = words[i]
            last = 0
            this = 0
            
            while last < len(last_word) and this < len(this_word):
                
                if m[last_word[last]] > m[this_word[this]]:
                    return False
                elif m[last_word[last]] < m[this_word[this]]:
                    break
                else:
                    last += 1
                    this += 1
            
            # this word is shorted
            if last >= len(this_word):
                return False

        return True