''' You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string. '''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []
        
        while i < m or j < n:
            if i < m:
                result.append(word1[i])
                i += 1
                
            if j < n:
                result.append(word2[j])
                j += 1
                
        return "".join(result)
    
