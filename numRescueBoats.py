"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

######Example_1:######

Input: 
    people = [1,2], 
    limit = 3

Output: 1

Explanation: 1 boat (1, 2)


######Example_2:######

Input: 
    people = [3,2,2,1], 
    limit = 3
    
Output: 3

Explanation: 3 boats (1, 2), (2) and (3)


########Example_3:########

Input: 
    people = [3,5,3,4], 
    limit = 5
    
Output: 4

Explanation: 4 boats (3), (3), (4), (5)
 

######Constraints:######

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""

"""
Understanding the Problem

- An array people, where people[i] is the weight of the i-th person.
- An integer limit, the maximum weight a boat can carry.
- Each boat can carry at most two people at once, as long as their combined weight is ≤ limit.
- I need to return the minimum number of boats needed to carry everyone.

"""

"""
Strategy (Greedy + Two Pointers):
- Sort the people array.
- Use two pointers:
    - One (light) starting at the beginning (lightest).
    - One (heavy) starting at the end (heaviest).
- Try to pair the lightest and heaviest. If they fit, move both pointers. If not, move just the heavy one.
- Count each move as a boat.
"""

def numRescueBoats(people, limit):
    people.sort()
    
    light = 0
    heavy = len(people) -1
    boats = 0
    
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1
    return boats


print(numRescueBoats([3, 2, 2, 1], 3))    # Expected: 3
print(numRescueBoats([3, 5, 3, 4], 5))    # Expected: 4
print(numRescueBoats([1, 2], 3))          # Expected: 1
print(numRescueBoats([1, 2, 2, 3], 3))    # Expected: 3
print(numRescueBoats([5, 1, 4, 2], 6))    # Expected: 2
print(numRescueBoats([1, 1, 1, 1], 2))    # Expected: 2
print(numRescueBoats([2, 2, 2, 2], 3))    # Expected: 4
        