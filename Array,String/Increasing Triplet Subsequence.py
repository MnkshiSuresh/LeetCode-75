'''Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exists, return false.'''

def triplets(a):
    count=0
    
    i=0
        
    while i<len(a)-2:
        if a[i]<a[i+1]<a[i+2]:
            count=1
            break
        i=i+1
    
    if count==1:
        print("true") 
    else: 
        print("false")
                    
                    

a = [2,1,5,0,4,6]
triplets(a)
