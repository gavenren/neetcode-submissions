class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            time = 0

            for pile in piles:
                time += (pile + m - 1) // m

            if time > h:
                l = m + 1
            else:
                r = m - 1

        return l