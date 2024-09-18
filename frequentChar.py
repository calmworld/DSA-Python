"""
Write a function, most_frequent_char, that takes in a string as an argument. 
The function should return the most frequent character of the string. 
If there are ties, return the character that appears earlier in the string.
You can assume that the input string is non-empty.
"""

"""
# 1 - Approach :

##Step 1: Sorting the String:

    - The function uses the sorted function to sort the characters in the string s.

    - The key parameter of the sorted function is set to a lambda function:
        lambda x: (s.count(x), s.index(x)).
            - s.count(x) counts the number of occurrences of the character x in the string s.
            - s.index(x) finds the first occurrence of the character x in the string s.

    - The sorted function sorts the characters based on a tuple (s.count(x), s.index(x)).
        - This means characters are primarily sorted by their frequency (s.count(x)).
        - In case of a tie (characters with the same frequency), they are sorted by their first occurrence (s.index(x)).

##Step 2: Reverse Sorting:

The reverse=True parameter is used to sort the characters in descending order (moving down a scale of quality).
This ensures that the most frequent character comes first in the sorted list.
"""

def most_frequent_char(s):
    return sorted(s, key=lambda x: (s.count(x), s.index(x)), reverse=True)[0]


print(most_frequent_char("abca")) # a
print(most_frequent_char("abbab")) # b
print(most_frequent_char("hello")) # l
print(most_frequent_char("zzz")) # z