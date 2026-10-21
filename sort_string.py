
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Check if already sorted
        sorted_str = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_str = False
                break

        if sorted_str:
            return 0

        # Cannot sort an unsorted string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum is at the beginning or maximum at the end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Minimum or maximum occurs in the middle
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Minimum is at the end and maximum at the beginning
        return 3
