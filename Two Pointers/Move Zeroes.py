'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''

def zeros(a):
    left = 0
    right = 0
    while right<len(a):
        if a[right]!=0:
            a[left],a[right] = a[right],a[left]
            left += 1
        right += 1    
    
    print(a)
    
    
    
    
    
array = [0,1,0,0,3,12]
zeros(array)
