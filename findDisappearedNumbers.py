"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

from typing import List

# Method 1 - Optimal with O(1) extra space complexity and O(n) runtime complexity
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    for x in nums:
        index = (x - 1) % n # his gives the zero-based index corresponding to the value x.
        # Add n to the value at this index in nums.
        nums[index] += n # This marks the presence of the number x in the original list.
    
    #  Find the numbers that are missing from the original list:
    # Use a list comprehension to generate a list of numbers from 1 to n. 
    # For each index i in nums, if the value at that index is less than or equal to n, 
    # it means the number i + 1 is missing from the original array.
    return [i + 1 for i, x in enumerate(nums) if x <= n]



# Method 2 - (Using Auxiliary Array)
# def findDisappearedNumbers(nums: List[int]) -> List[int]:
#     allNums = [0] * len(nums) # Initialize a list of 0s with the same length as nums
    
#     for i in nums:
#         # Set the value at index i - 1 to i in allNums.
#         allNums[i - 1] = i # This marks the presence of the number i in the original list.
    
#     # Use a list comprehension to generate a list of numbers from 1 to len(allNums) 
#     # where the corresponding index in allNums is still zero.
#     # If allNums[i] is zero, it means the number i + 1 is missing from the original nums list.
#     return [i + 1 for i in range(len(allNums)) if allNums[i] == 0]



# Method 3 - In-place Modification
# def findDisappearedNumbers(nums: List[int]) -> List[int]:
    # for x in nums:
    #     index = abs(x) - 1
    #     nums[index] = -abs(nums[index])
    
    # return [i + 1 for i, x in enumerate(nums) if x > 0]



# Method 4 - Hash Set
# def findDisappearedNumbers(nums: List[int]) -> List[int]:
#     return list(set(range(1, len(nums) + 1)) - set(nums))




nums_a = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums_a))


nums_b = [1,1]
print(findDisappearedNumbers(nums_b))