class Solution():
    def pancakeSort(self, A):
        res = []

        N = len(A)
        B = sorted(range(1, N + 1), key=lambda i: -A[i - 1])
        print(B)
        for i in B:
            for f in res:
                if i <= f:
                    i = f + 1 - i
            res.extend([i, N])
            N -= 1

        return res


if __name__ == '__main__':
    solu = Solution()
    A = [3, 2, 4, 1]
    print(solu.pancakeSort(A))
