"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# from itertools import zip_longest

# Method 1 - using itertools.zip_longest to merge the two strings in an alternating order
# def mergeAlternately(word1: str, word2: str) -> str:
#     result = ""
#     return result.join([x for y in zip_longest(word1, word2, fillvalue='') for x in y])



# Method 2 - Using a for loop to iterate through the two strings and merge them in an alternating order
# def mergeAlternately(word1: str, word2: str) -> str:
#     result = ""
#     for i in range(min(len(word1), len(word2))):
#         result += word1[i] + word2[i]
#     if len(word1) > len(word2):
#         result += word1[len(word2):]
#     else:
#         result += word2[len(word1):]
#     return result


# Method 3 - Using itertools.zip to merge the two strings in an alternating order
def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    result = ""

    for a, b in zip(word1, word2): # zip built-in-func: Iterates over several iterables in parallel
        merged.append(a + b)
    
    # Handle Remaining Characters
    merged.append(word1[len(word2):]) # Append the remaining characters from word1 if word1 is longer than word2.
    merged.append(word2[len(word1):]) # Append the remaining characters from word2 if word2 is longer than word1.

    return result.join(merged) # Join the merged list into a string.





word_a = "abc"
word_b = "pqr"
print(mergeAlternately(word_a, word_b)) # Output: "apbqcr"

word_c = "ab"
word_d = "pqrs"
print(mergeAlternately(word_c, word_d)) # Output: "apbqrs"

word_e = "abcd"
word_f = "pq"
print(mergeAlternately(word_e, word_f)) # Output: "apbqcd"