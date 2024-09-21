from typing import Optional
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- `-10^5 <= Node.val <= 10^5`
- pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


"""
Strategies to Tackle the Problem

Hash Table Method:
This approach involves storing visited nodes in a hash table. During traversal, 
if a node is encountered that already exists in the hash table, a cycle is confirmed.

Two-Pointers Method (Floyd's Cycle-Finding Algorithm):
Also known as the "hare and tortoise" algorithm, this method employs two pointers that move at different speeds. 
If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's existence.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
# Hash Table Method:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = set()
    #     curr = head
        
    #     while curr:
    #         if curr in visited:
    #             return True
    #         visited.add(curr)
    #         curr = curr.next
    #     return False
    

# Two-Pointers Method (Floyd's Cycle-Finding Algorithm):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        
        
        while slow_pointer and fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

# Manually create the linked list [3, 2, 0, -4] and create a cycle at position 1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Create cycle here

# Create an instance of the Solution class
solution = Solution()

# Call the hasCycle method on the instance
print(solution.hasCycle(node1)) # True