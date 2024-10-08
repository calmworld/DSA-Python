"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


"""
Method 1: Using String Reversal

Space Complexity: 
It creates a new reversed string, which requires additional space proportional to the length of the string (O(n) space complexity).

Reverse the String: 
The expression s[::-1] uses Python's slicing syntax to reverse the string s. 
The slicing syntax s[start:stop:step] allows you to specify a start index, a stop index, and a step.
By setting the step to -1, it reverses the string.

Compare the Strings: 
The code then checks if the original string s is equal to the reversed string s[::-1].

Return the Result: 
If the original string is equal to the reversed string, it means the string is a palindrome, 
and the function returns True. Otherwise, it returns False.
"""

# class Solution:
#     def check_if_palindrome(self, s: str) -> bool:
#         if s == s[::-1]:
#             return True
#         return False

# # Create an instance of the Solution class
# solution = Solution()

# # Call the check_if_palindrome method on the instance
# print("racecar is", solution.check_if_palindrome("racecar")) # True
# # print("rotator is", solution.check_if_palindrome("rotator")) # True
# # print("hello is", solution.check_if_palindrome("plant")) # False
# print("A man, a plan, a canal: Panama is", solution.check_if_palindrome("A man, a plan, a canal: Panama")) # True



"""
Method 2: Using Two Pointers

Space Complexity: 
It uses constant space (O(1) space complexity) since it only uses two pointers.

This method uses two pointers to compare characters from the start and end of the string, moving towards the center.
If all corresponding characters are equal, the string is a palindrome. Otherwise, the string is not a palindrome.
"""

# class Solution:
#     def check_if_palindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
        
#         return True

# # Create an instance of the Solution class
# solution = Solution()

# # Call the check_if_palindrome method on the instance
# print("kayak is", solution.check_if_palindrome("kayak")) # True
# print(" is", solution.check_if_palindrome("")) # True
# print("A man, a plan, a canal: Panama is", solution.check_if_palindrome("A man, a plan, a canal: Panama")) # True



"""
Method 3: Using ~ NOT operator 

Time Complexity: O(n), where n is the length of the string, due to the normalization and comparison steps.
Space Complexity: O(n), due to the creation of the normalized list.


This method involves normalizing the string by removing non-alphanumeric characters -> c.isalnum(),
and converting it to lowercase -> c.lower(), 

then, using a generator expression to compare characters from the start and end of the string:
range(len(s) // 2): Iterates over the first half of the string.
s[i] == s[~i]: Compares the character at index i with the character at index ~i. 


The ~ operator is the bitwise NOT operator, 
It's used to get the index from the end of the list (~i is equivalent to -(i+1)).

it performs logical negation on a given number by flipping all of its bits: ~x == -x-1 , ~0 == -1, ~1 == -2 and etc.
"""

class Solution:
    def check_if_palindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s) // 2))
        

# Create an instance of the Solution class
solution = Solution()

# Call the check_if_palindrome method on the instance
print("The string 'kayak' is a palindrome:", solution.check_if_palindrome("kayak")) # True
print("An empty string should return true:", solution.check_if_palindrome("")) # True
print("The string 'A man, a plan, a canal: Panama' is a palindrome:", solution.check_if_palindrome("A man, a plan, a canal: Panama")) # True