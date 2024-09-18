"""
Consider a long alley with a N number of doors on one side. All the doors are closed initially. 

You move to and fro in the alley changing the states of the doors as follows: 
- you open a door that is already closed and you close a door that is already opened. 
- You start at one end go on altering the state of the doors till you reach the other end 
- and then you come back and start altering the states of the doors again.

In the first go, you alter the states of doors numbered 1, 2, 3, , n.
In the second go, you alter the states of doors numbered 2, 4, 6
In the third go, you alter the states of doors numbered 3, 6, 9
You continue this till the Nth go in which you alter the state of the door numbered N.
You have to find the number of open doors at the end of the procedure.

 

Example 1:

Input:
N = 2
Output:
1
Explanation:
Initially all doors are closed.
After 1st go, all doors will be opened.
After 2nd go second door will be closed.
So, Only 1st door will remain Open.
Example 2:

Input:
N = 4
Output:
2
Explanation:
Following the sequence 4 times, we can
see that only 1st and 4th doors will
remain open.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfOpenDoors() which takes an Integer N as input and returns the answer.

 

Expected Time Complexity: O(√N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 1012
"""

# Method 1: Importing math module and using math.sqrt() function

# import math

# class Solution:
#     def noOfOpenDoors(self, N):
#         return int(math.sqrt(N))



# Method 2: Using the math.sqrt() function

# class Solution:
#     def noOfOpenDoors(self, N):
#         return int(N**0.5)



# Method 3: 

"""
- We will represent our hallway of doors with a list, 
a mutable sequence of Boolean values to represent whether the doors are opened or closed ( True or False, respectively).

- Sicne we would be toggling every door, I used a for loop to iterate over the sequence.
so need to track which door I was on with an index, which is why I used the range() function
"""

# class Solution:
#     def noOfOpenDoors(self, N):
        
#         n = 100
#         doors = [False] * n

#         # first pass over doors 
#         """
#         This left me with a list of True values, and I spent a few minutes just trying to 
#         figure out what the second, third, fourth, and so on iterations would look like.
#         """
        
#         # for i in range(0, n):
#         #     doors[i] = not doors[i]
#         #     print(doors)

#         """
#         It became apparent that the use of nested for loops would become necessary to completing this algorithm, 
#         since I would need to iterate over all of the doors 100 times, while keeping track of which iteration I was on.

#         Basically, the outer loop iterates over the list of doors 100 times, with a range from 0 to 100. 
#         As a reminder, the Python range() function excludes the upper boundary of the range, and all lists are zero-indexed by default.
#         """
#         # nested for loop is needed.
#         for x in range(0, n):
#                 """
#                 The inner loop is where the interesting part of the algorithm lies. Here, the elements that are toggled are 
#                 decided by changing the range that the for loop will use. 
#                 In every iteration, the starting point is equal to the index of the outer loop, to simulate the “every nth” door condition.
#                 """
#                 # in range method always go 1 index further than the n value you have
#                 for y in range(x, n, x+1):
#                     # change the value of this doors
#                     doors[y] = not doors[y]
#                     print(doors)
#                     # print("x: ", x, "y: ", y)



# Create an instance of the Solution class
# solution = Solution()

# call the noOfOpenDoors method on the instance
# print(solution.noOfOpenDoors(100)) # 10
# print(solution.noOfOpenDoors(2)) # 1
# print(solution.noOfOpenDoors(4)) # 2

# quick printout of open doors
# print("\nFinal State of doors:\n")
# for index,door in enumerate(doors):
#     if door: # evaluates door as a Boolean value
#         print(f'{index+1}: Open; Square: {int(sqrt(index+1))}')



# Method 4: return indices of open doors

# class Solution:
#     def openDoors(self, Num):
        
#         n = Num
#         doors = [False] * n
#         opened = []

#         for x in range(0, n):
#             for y in range(x, n, x+1):
#                 doors[y] = not doors[y]

#         for j in range(0, n):
#             if doors[j] != False:
#                 opened.append(j)

#         return opened


# Method 5: return indices of open doors

class Solution:
    def openDoors(self, Num):
        
        n = Num
        doors = [False] * n
        opened = []

        for x in range(0, n):
            for y in range(x, n, x+1):
                doors[y] = not doors[y]

        for j in range(0, n):
            if doors[j] is not False:
                opened.append(j)

        return opened

# Create an instance of the Solution class
solution = Solution()

# call the noOfOpenDoors method on the instance
print(solution.openDoors(100)) # 10