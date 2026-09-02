class Solution:
    # approach 1: two loops O(n^2)
    # approach 2: we will use same concept of trapping rain water;
    # will use two pointer l and r and track left min and right maximum so far and shift l and r towrds each other ,but if we do l++ and r-- simultaneosly we are assuming that the buying period is only till len/2 and selling period is after len/2 half . but that's not the case. 
    # approach 3: 2pointers , but this time l,r denotes buying and selling day day respectively, why it does not occured to be before that there is no need to set l and r on opposite ends , who said to do that . # okay , so idea is we start from 0,1 , if there is loss, so we can safely move our buying day l to r . because if we are facing loss then buying on that selling day will definately give us more profit than buying on this day , if there is profit we can safely move r+1 , and keep on recording maxprofit , untill we encounter loss, 
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r<len(prices):
            if prices[r]>=prices[l]:
                profit = max(profit,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
           
            
            

        return profit
        