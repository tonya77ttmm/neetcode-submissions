class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #WE need to use a sliding window of size of len(s1) to traverse s2
        #to compare if there's a substring of s2 that is a permutation of s1
        #That should be O(n) * O(n)=O(n2)
        #(to compare if two strings have the exact same letters, space O(26), and 
        #time complexity O(n) ) 
        #The recommended space complexity is O(1), so 2 array to represent the frequence
        #of each letter in 2 strings respectively
        #If the recommended time complexity is O(n), it means, when we check if the substring 
        #of s2 is a permutation of s1, we can't iterate these substring of s2 and sting s1 every time
        #we need a way to record if adding a new letter and removing an old letter gives us more matches

        if len(s1)>len(s2):
            return False
        matches=0
        s1_freq=[0]*26
        s2_freq=[0]*26

        for c in s1:
            s1_freq[ord(c)-ord('a')]+=1
        for i in range(len(s1)):
            s2_freq[ord(s2[i])-ord('a')]+=1
            
        for i in range(26):
            matches+=1 if s1_freq[i]==s2_freq[i] else 0

        l=0
        for r in range(len(s1),len(s2),1):
            if matches==26:
                return True
            #expanding the window
            index=ord(s2[r])-ord('a')
            s2_freq[index]+=1
            if s2_freq[index]==s1_freq[index]:
                matches+=1
            elif s2_freq[index]-1 ==s1_freq[index]:
                matches-=1
            
            #shrinking the window
            index=ord(s2[l])-ord('a')
            s2_freq[index]-=1
            if s2_freq[index]==s1_freq[index]:
                matches+=1
            elif s2_freq[index]+1==s1_freq[index]:
                matches-=1
            l+=1

        return matches==26






