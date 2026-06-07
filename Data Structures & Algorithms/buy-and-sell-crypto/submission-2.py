class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        maxPrice=0
        # for i in range(length-2,-1,-1):
        #     maxPrices[i]=max(maxPrices[i+1],prices[i+1])
        profit=0
        for i in range(length-2,-1,-1):
            maxPrice=max(maxPrice,prices[i+1])
            curpro=maxPrice-prices[i]
            if curpro>0:
                profit=max(profit,curpro)
        return profit



        