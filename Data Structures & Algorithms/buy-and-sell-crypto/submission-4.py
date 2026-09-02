class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin,profit = prices[0],0
        
        for i in range(len(prices)):
            lmin = min(prices[i],lmin)
            profit = max(profit,prices[i]-lmin)
        return profit