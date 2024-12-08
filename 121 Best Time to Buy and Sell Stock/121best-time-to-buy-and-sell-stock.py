class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_price = float('inf')
        for price in prices:
            if(min_price > price):
                min_price = price
            profit = price - min_price
            maxProfit = max(profit, maxProfit)
        return maxProfit
