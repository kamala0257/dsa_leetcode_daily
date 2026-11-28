from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Count frequency of each factor (1 <= factor <= n)
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1

        # Calculate M[f]: number of OTHER items j where f divides factor_j
        # Using harmonic series in O(N log N)
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                total_divisible = 0
                for mult in range(f, n + 1, f):
                    total_divisible += freq[mult]
                # Exclude the item itself (i != j)
                multiples[f] = total_divisible - 1

        # Sort items by price ascending
        items.sort(key=lambda x: x[1])

        min_price = items[0][1]
        total_items = 0

        # Greedily buy 2-for-1 bonus copies while price < 2 * min_price
        for f, price in items:
            if price >= 2 * min_price:
                break

            max_bonus_copies = multiples[f]
            if max_bonus_copies > 0 and budget >= price:
                can_buy = min(max_bonus_copies, budget // price)
                total_items += can_buy * 2
                budget -= can_buy * price

        # Spend remaining budget on the cheapest single item
        total_items += budget // min_price

        return total_items
