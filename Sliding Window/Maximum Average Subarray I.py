    def findMaxAverage(nums, k):
    n = len(nums)
    window_sum = sum(nums[:k])  
    max_sum = window_sum
    
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]  
        max_sum = max(max_sum, window_sum)  
        
    return max_sum / k 

# Test the function
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75
