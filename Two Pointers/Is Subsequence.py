'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.'''

def isSubsequence(s1, s2):
    s1_start = 0
    s2_start = 0
    
    while s1_start < len(s1) and s2_start < len(s2):
        if s1[s1_start] == s2[s2_start]:
            s1_start += 1
        s2_start += 1
    
    return s1_start == len(s1)

# Example usage:
s1 = "gac"
s2 = "ahbgdc"
print(isSubsequence(s1, s2)) 
