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

class Solution:
    def check_if_palindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False

# Create an instance of the Solution class
solution = Solution()

# Call the check_if_palindrome method on the instance
print("racecar is", solution.check_if_palindrome("racecar")) # True
print("rotator is", solution.check_if_palindrome("rotator")) # True
print("hello is", solution.check_if_palindrome("plant")) # False


"""

"""
class Solution:
    def check_if_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Create an instance of the Solution class
solution = Solution()

# Call the check_if_palindrome method on the instance
print("kayak is", solution.check_if_palindrome("kayak")) # True
print("hello is", solution.check_if_palindrome("hello")) # False
