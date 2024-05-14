'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.'''


def toffies(a,e):
    maxt = max(a)
    b = []
    for i in range(len(a)):
        a[i] += e
        if a[i]>=maxt:
            b.append("true")
            
        else:
            b.append("false")
    
    print(b) 
 


a = [12,1,12]
e = 10
toffies(a,e)
