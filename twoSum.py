"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List

# Approach 1: Using Brute Force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)

#         for i in range(n - 1):
#             for j in range( i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []



# Approach 2: Using a Two-Pass Hash Table
"""
A dictionary numMap is created to store the indices of the numbers in the list nums.

First Pass - Building the Hash Table: 
    - Iterate through the list nums and populate the numMap dictionary.
    - For each element nums[i], store its index i in the dictionary with the element itself as the key.
    - This allows quick look-up of any number's index in the list.

Second Pass - Finding the Two Numbers:
    - Iterate through the list nums again.
    - For each element nums[i], calculate its complement as target - nums[i].
    - Check if the complement exists in the numMap dictionary and ensure that 
    the complement is not the same element as nums[i] (i.e., numMap[complement] != i).
    - If both conditions are met, return the indices [i, numMap[complement]].
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)

#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i

#         # Find the two numbers
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]

#         return []




# Approach 3: Using a One-Pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        
        return []


# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method on the instance
print(solution.twoSum([2,7,11,15], 9)) # [0, 1]
print(solution.twoSum([3,2,4], 6)) # [1, 2]
print(solution.twoSum([3,3], 6)) # [0, 1]


