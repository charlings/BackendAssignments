def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example 1
print(two_sum([2,7,11,15], 9))   # Output: [0, 1]

# Example 2
print(two_sum([3,2,4], 6))       # Output: [1, 2]

# Example 3
print(two_sum([3,3], 6))         # Output: [0, 1]
