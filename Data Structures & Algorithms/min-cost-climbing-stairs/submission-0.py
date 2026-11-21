class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i] represents the minimum cost from step 0 to i
        #dp[0]=0
        #dp[1]=0
        #dp[2]=min(2,1)=1
        #dp[3]=min(4,dp[1]+2)=2
        #dp[n]=min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2]
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2, n+1,1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]