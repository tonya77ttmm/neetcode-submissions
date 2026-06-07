class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        s_freq=defaultdict(int)
        t_freq=defaultdict(int)
        matches=0
        for c in t:
            t_freq[c]+=1
        # for i in range(len(t)):
        #     s_freq[s[i]]+=1
        unique_t=len(t_freq)
        # for k in t_freq.keys():
        #     matches+=1 if t_freq[k]<=s_freq[k] else 0
        result=""
        shortest_len=float("inf")
        l=0
        for r in range(0,len(s),1):
            #expand the window
            index=s[r]
            s_freq[index]+=1
            if s_freq[index]==t_freq[index]:
                matches+=1
            while matches==unique_t:
                #update result
                if r-l+1<shortest_len:
                    shortest_len=min(shortest_len, r-l+1)
                    result=s[l:r+1]
                #shrink the window
                index=s[l]
                l+=1
                s_freq[index]-=1
                #match before, after removing , not match
                if s_freq[index]+1 ==t_freq[index]:
                    matches-=1
                #match before, after removing, still match, no need to change match
                #not match before, after removing, not match, still no need to change match
                
            
        return result
    


        