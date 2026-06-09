class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time? (10-4)/2=3. (10-7)/1=3.  (10-1)/2=4.5. (10-0)/1=10
        #set (time)= numbers of fleet
        #car catch up another car
        #sort all positions in decreasing order
        #next greater speed mono decreasing stack
        #
        #time of fleets mono increasing stack
        #[5,6,7,8,]
        #[10,10]
        #if current time >stack[-1] time:
        #stack.append(current time)
        cars=[[] for _ in range(len(speed))]
        for i in range(len(speed)):
            cars[i]=tuple([position[i],speed[i]])
        cars.sort(reverse=True)

        time=[0]*len(speed)
        for i,car in enumerate(cars):
            position,speed=car
            time[i]=(target-position)/speed
        stack=[]
        stack.append(time[0])
        for i in range(1,len(time),1):
            if stack and time[i]>stack[-1]:
                stack.append(time[i])
        return len(stack)
            
            

