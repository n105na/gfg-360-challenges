class Solution:
    def minCost(self, heights, cost):
        pairs = sorted(zip(heights, cost))  # Step 1: sort by height
        total = sum(cost)  # Step 2: total cost weight

        prefix = 0
        for h, c in pairs:
            prefix += c
            if prefix >= total / 2:
                median = h
                break

        return sum(abs(h - median) * c for h, c in pairs)

