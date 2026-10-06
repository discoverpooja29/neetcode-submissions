class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        max_profit = 0

        for k in range(0, len(prices)):
            if i < k and prices[i] > prices[k] and k < len(prices)-1:
                i = k

            if i > j or (j < k and prices[j] < prices[k]):
                j = k

            max_profit = max(max_profit, prices[j] - prices[i])
            
        return max_profit