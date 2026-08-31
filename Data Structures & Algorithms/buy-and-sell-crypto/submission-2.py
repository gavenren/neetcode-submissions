class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        lowest_price = prices[0]
        highest_price = prices[1]

        for i in range(0, len(prices)-1):
            if prices[i+1] <= prices[i]:
                continue
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if prices[i+1] > highest_price:
                highest_price = prices[i+1]
            if highest_price - lowest_price > profit:
                profit = highest_price - lowest_price
                highest_price = 0
        return profit
