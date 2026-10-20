class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for b in range(0, n, k):
                desc = 0
                lo = hi = nums[b]
                for i in range(b, b + k - 1):
                    x, y = nums[i], nums[i + 1]
                    if x > y:
                        desc += 1
                    if y < lo:
                        lo = y
                    if y > hi:
                        hi = y
                if k > 1 and nums[b + k - 1] > nums[b]:
                    desc += 1
                if desc > 1 or lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                total += k
        return total
