class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_prices = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_prices:
                min_prices = price
            elif price - min_prices > max_profit:
                max_profit = price - min_prices
        return max_profit 