"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List

# Method 1: Using a hash set - Best solution
# def containsDuplicate(nums: List[int]) -> bool:
#     seen = set()
#     for x in nums:
#         if x in seen:
#             return True
#         seen.add(x)
#     return False


# Method 2: Using a hash map
def containsDuplicate(nums: List[int]) -> bool:
    seen = {} # Initialize an Empty Dictionary to store the frequency of each element
    
    for x in nums:
        if x in seen and seen[x] >= 1:
            return True
        
        # Update the count of the current element x in the dictionary seen.
        # seen.get(x, 0) retrieves the current count of x from the dictionary.
        # If x is not in the dictionary, it returns 0.
        # then it increments the count by 1.
        seen[x] = seen.get(x, 0) + 1
    return False


# Method 3: 
# def containsDuplicate(nums: List[int]) -> bool:
#     return len(nums) > len(set(nums))


# Method 4: Using the built-in max function
"""
    The function uses the built-in max function to find the mode of the
    list (number with highest frequency). If the count of the number with the highest 
    frequency is greater than 1, the list has duplicates.
"""
# def containsDuplicate(nums: List[int]) -> bool:
#     if nums is None or len(nums) == 0:
#         return False
    
#     # Find the Most Frequent Element
#     n = max(set(nums), key=nums.count)

#     # Check for Duplicates
#     return nums.count(n) > 1





nums_a = [1, 2, 3, 1]
print(containsDuplicate(nums_a))  # True

nums_b = [1, 2, 3, 4]
print(containsDuplicate(nums_b))  # False

nums_c = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums_c))  # True

nums_d = [0]
print(containsDuplicate(nums_d))  # False

nums_e = []
print(containsDuplicate(nums_e))  # False
