class Twitter:

    def __init__(self):
        self.followMap=defaultdict(set) #{"userid":set(followeeIds),}
        self.tweetMap=defaultdict(list)  #{"userId":[(count,tweetId)]}
        self.count=0 #incremented with each tweet, tracks the order of tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.tweetMap[userId].append((self.count,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        #the bigger the counter, the closer the tweet
        #get all followeeIds
        self.followMap[userId].add(userId)
        res=[]
        heap=[]
        #get the closest tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index=len(self.tweetMap[followeeId])-1
                count, tweet=self.tweetMap[followeeId][index] #the closest tweet
                heap.append((-count,tweet,followeeId, index-1))
        heapq.heapify(heap)
        while heap and len(res)<10:
            count,tweet,followeeId,index= heapq.heappop(heap)
            res.append(tweet) #store the closest tweet
            if index>=0:
                count,tweet=self.tweetMap[followeeId][index]
                heapq.heappush(heap,(-count,tweet,followeeId, index-1))
        return res

    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
