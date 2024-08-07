''' Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. '''

def divisor(s1, s2):
    shortest_str = min(s1, s2, key=len)
    longest_divisor = ""

   
    for i in range(len(shortest_str)):
        for j in range(i + 1, len(shortest_str) + 1):
            substring = shortest_str[i:j]
            if s1.count(substring) > 0 and s2.count(substring) > 0:
                if len(substring) > len(longest_divisor):
                    longest_divisor = substring

    return longest_divisor

s1 = "meenakshi"
s2 = "meenu"
print(divisor(s1, s2))
