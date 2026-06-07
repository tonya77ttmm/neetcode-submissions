class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            w_len=len(word)
            result+=str(w_len)
            result+="#"
            result+=word
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i< len(s):
            w_len=0
            while s[i]!="#":
                w_len=w_len*10+int(s[i])
                i+=1
                # 5#abcde3#

            result.append(s[i+1:i+w_len+1])
            i=i+w_len+1
        return result