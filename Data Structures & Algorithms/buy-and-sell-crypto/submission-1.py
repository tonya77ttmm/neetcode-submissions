class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        maxPrices=[0]*length
        for i in range(length-2,-1,-1):
            maxPrices[i]=max(maxPrices[i+1],prices[i+1])
        profit=0
        for i in range(length):
            curpro=maxPrices[i]-prices[i]
            if curpro>0:
                profit=max(profit,curpro)
        return profit



        