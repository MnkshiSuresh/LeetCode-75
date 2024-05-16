'''You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.'''

def max_operations(nums, k):
    nums.sort()  
    left, right = 0, len(nums) - 1
    max_ops = 0

    while left < right:
        if nums[left] + nums[right] == k:
            max_ops += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1

    return max_ops

nums = [1, 2, 3, 4, 5]
k = 8
print(max_operations(nums, k))  
