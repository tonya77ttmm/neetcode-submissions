class TimeMap:

    def __init__(self):
        #{"alice":[(1,"happy"),(3,"sad"))]}
        self.d=defaultdict(list)



    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        #dict["key"]   search this list  the first  timestamp <=time stamp
        # T T T  F F F  last true problem
        #binary search timestamps

        #no value or 3,4,5 get "1", no prev_stamp<= cur_timestamp
        if not self.d[key] or self.d[key][0][0]>timestamp:
            return ""
        # l_time=d["key"][0][0]
        # r_time=d["key"][-1][0]
        r_index=len(self.d[key])-1
        l_index=0

        while l_index<r_index:
            # mid_time=(l+r+1)//2
            mid_index=(l_index+r_index+1)//2
            if self.d[key][mid_index][0]<= timestamp:
                l_index=mid_index
            else:
                r_index=mid_index-1
        return self.d[key][l_index][1]
            
