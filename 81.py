
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if len(A) == 0:
            return False
        low = 0
        high = len(A) - 1
        while low < high:
            mid = low + (high - low) / 2
            if A[mid] == target:
                return True
            if A[low] < A[mid]:
                if A[low] <= target < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif A[low] > A[mid]:
                if A[mid] < target <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        if A[low] == target:
            return True
        return False
