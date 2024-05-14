'''Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group 
lengths that are 10 or longer will be split into multiple characters in chars.'''

def compress(array):
    b = []
    i = 0
    while i<len(array):
        letter = array[i]
        b.append(array[i])
        count=0
        while i < len(array) and array[i] == letter:
            count+=1
            i=i+1
        b.append(count)
    print(b)               

array =["a","a","b","b","c","c","c"]
compress(array)
