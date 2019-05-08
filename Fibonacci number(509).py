class Solution:
    def fib(self, N):
        array =[i for i in range(N+1)]
        return self.fibola(array, N)

    def fibola(self, array, N):
        if N <= 1:
            return N
        array[N] = self.fibola(array, N-1) + array[N-2]
        return array[N]
