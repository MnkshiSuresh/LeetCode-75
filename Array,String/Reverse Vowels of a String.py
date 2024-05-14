'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''

def vowels(a):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_string = ""
    
    for letter in a:
        if letter in vowels:
            vowel_string += letter
    
    print(vowel_string)
    
    
    reversed_vowels = ''.join(reversed(vowel_string))
    
    
    result = ""
    vowel_index = 0
    
    for letter in a:
        if letter in vowels:
            result += reversed_vowels[vowel_index]
            vowel_index += 1
        else:
            result += letter
    
    print(result)

sent = "leetcode"
vowels(sent)
