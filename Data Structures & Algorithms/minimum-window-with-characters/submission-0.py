class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
       # first expand r to get the valid window, then shrink window by increasing l
       #keep recording the valid window, 
       #until the charaters in the window doesn't include t
       #then break, continue to move r
        freq_t=Counter(t)
        window={}
        have=0
        need=len(freq_t)
        res=[-1,-1]
        reslen=float("infinity")
        l=0
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in freq_t and window[s[r]]==freq_t[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in freq_t and window[s[l]]<freq_t[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("infinity") else""
    


        