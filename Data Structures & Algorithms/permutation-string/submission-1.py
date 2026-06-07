class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #r, l  
        #if l not in s1, l++
        #else r=l:
            #while r-l+1 <=s1.length && r<s2.length && [r] in s2
            #if(r-l+1)==s1.length
                #?return true: break
            #else:
                 #r++
        #substring={}
        #def (s1, s2):
            #count=[0]*26
            #for c in s1
             #count[ord(c)-ord('a')]++
            #for c in s2:
                #cur=ord(c)-ord('a')
                #count[cur]--;
                #if ount[cur]<0:
                    #return False
            #return True
        s1_len=len(s1)
        s2_len=len(s2)
        for l in range(s2_len):
            if s2[l] not in s1:
                continue
            else:
                r=l
                while (r<s2_len) and (s2[r] in s1) and  ((r-l+1)<=s1_len):
                    if ((r-l+1)==s1_len):
                        check=self.isMutation(s1,s2[l:r+1])
                        if check:
                            return True
                        else:
                            break
                    else:
                        r+=1
        return False

    def isMutation(self, s1:str ,s2:str)->bool:
            count=[0]*26
            for c in s1:
                count[ord(c)-ord('a')]+=1
            for c in s2:
                cur=ord(c)-ord('a')
                count[cur]-=1
                if count[cur]<0:
                    return False
            return True    
        