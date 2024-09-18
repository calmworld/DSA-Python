"""
Write a function, anagrams, that takes in two strings as arguments. 
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.
"""

# Method 1: Using the sorted() function

# def anagrams(s1, s2):
#     return sorted(s1) == sorted(s2)


# Method 2: Using the Counter() function from the collections module

# from collections import Counter

# def anagrams(s1, s2):
#     return Counter(s1) == Counter(s2)


# Method 3: Using a dictionary
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

# def char_count(s):
#     count = {}
#     for char in s:
#         if char in count:
#             count[char] +=1
#         else:
#             count[char] = 1
#     return count

def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


print(anagrams("listen", "silent")) # True
print(anagrams("hello", "world")) # False
print(anagrams('restful', 'fluster')) # True
print(anagrams('elvis', 'lives')) # True
print(anagrams('restful', 'fluster')) # True
print(anagrams('po', 'popp')) # False
print(anagrams('pp', 'oo')) # False