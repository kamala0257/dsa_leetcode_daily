from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        sum_tree = [0] * (4 * n)
        sq_tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, l, r, val):
            length = r - l + 1
            sq_tree[node] = (sq_tree[node] + 2 * val * sum_tree[node] + val * val * length) % MOD
            sum_tree[node] = (sum_tree[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def push(node, l, r):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0
                
        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            sum_tree[node] = (sum_tree[2 * node] + sum_tree[2 * node + 1]) % MOD
            sq_tree[node] = (sq_tree[2 * node] + sq_tree[2 * node + 1]) % MOD

        last = {}
        ans = 0
        for i, x in enumerate(nums):
            l = last.get(x, -1) + 1
            update(1, 0, n - 1, l, i, 1)
            last[x] = i
            ans = (ans + sq_tree[1]) % MOD
            
        return ans
