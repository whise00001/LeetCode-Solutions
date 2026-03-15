class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_prices = prices[0]
        profit = 0

        for i in prices:
            if buy_prices > i :
                buy_prices = i
            profit = max(profit,i - buy_prices)
        
        return profit