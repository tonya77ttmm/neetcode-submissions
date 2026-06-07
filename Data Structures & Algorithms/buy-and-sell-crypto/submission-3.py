class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # A brute-force approach would be: 
        #for each selling day, iterate over all previous days 
        #to find the minimum buying price, which leads to O(n²) time.

#The optimized approach avoids this 
#by maintaining the minimum price seen so far 
#while scanning the array once. 
        profit=0
        min_price=float('inf')
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                profit=max(profit, price-min_price)
        return profit



        