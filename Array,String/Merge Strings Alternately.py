#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
#If a string is longer than the other, append the additional letters onto the end of the merged string.

def mergestrings(word1, word2):
    merged = ""
    max_len = max(len(word1), len(word2))
    for i in range(max_len):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
    return merged

word1 = "meenakshi"
word2 = "annathomas"
print(mergestrings(word1, word2))
