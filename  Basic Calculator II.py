class Solution(object):

    def calculate(self, s):
        """ :type s: str :rtype: int """
        def checkFun(x): return x if x.isdigit() or x in (
            '+', '-', '*', '/') else None  # checking if it is num or operator
        exp = filter(checkFun, re.split(r"(\D)", s))
        precedeTable = {'++': '>', '+-': '>', '+*': '<', '+/': '<', '+#': '>',
                        '-+': '>', '--': '>', '-*': '<', '-/': '<', '-#': '>',
                        '*+': '>', '*-': '>', '**': '>', '*/': '>', '*#': '>',
                        '/+': '>', '/-': '>', '/*': '>', '//': '>', '/#': '>',
                        '#+': '<', '#-': '<', '#*': '<', '#/': '<', '##': '='}
        stackOp = ['#']
        stackNum = []
        exp.append('#')  # append op with num
        i = 0
        while i < len(exp):
            e = exp[i]
            if e.isdigit():
                stackNum.append(int(e))
                i += 1
            else:
                if precedeTable[stackOp[-1] + e] == '<':
                    stackOp.append(e)
                    i += 1
                elif precedeTable[stackOp[-1] + e] == '>':
                    b = stackNum.pop()
                    a = stackNum.pop()
                    op = stackOp.pop()
                    if op == '+':
                        stackNum.append(a + b)
                    elif op == '-':
                        stackNum.append(a - b)
                    elif op == '*':
                        stackNum.append(a * b)
                    else:
                        stackNum.append(a / b)
                else:
                    stackOp.pop()  # prepare for next calculation
                    i += 1
        return stackNum[0]
