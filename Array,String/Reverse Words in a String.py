''' Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 

The returned string should only have a single space separating the words. Do not include any extra spaces. '''


def sentence(a):
    b = a.split(" ")
    print(b)
    
    c=list(reversed(b))
    print(c)
    result = " ".join(c)
    print(result)
    
    
    
    
    
  
sent = "leetcode is my fav"
sentence(sent)
