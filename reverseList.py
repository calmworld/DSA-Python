"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:
- The number of nodes in the list is the range [0, 5000].
- `-5000 <= Node.val <= 5000`
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Method 1 - Recursive Method:

# def reverseList(head):
#     if head is None or head.next is None:
#         return head
    
#     print(f"Initial_head_data##head.data: {head.data}")
    
#     # reverse the rest of linked list and put the 
#     # first element at the end
#     rest = reverseList(head.next)
#     print(f"BREAK------------------------------BREAK")
#     print(f"reversed_list##head: {head.data}")
#     print(f"BREAK------------------------------BREAK")
#     print(f"reveresed_list##head.next: {head.next.data}")
#     # print(f"first##rest: {rest.data}")
    

#     # Make the current head as last node of remaining linked list
#     head.next.next = head
#     print(f"BREAK------------------------------BREAK")
#     print(f"make_current_head_last_node_of_remaining_linked_list##head.next.next: {head.next.next.data}")
#     print(f"##head.next.next.next: {head.next.next.next.data}")
    
#     # Update next of current head to NULL
#     head.next = None
#     print(f"BREAK------------------------------BREAK")
#     print(f"Last##head.next: {head.data}")
    
#     return rest


# Method 2 - Iterative Method

def reverseList(head):
        prev = None  # Previous node starts as None
        curr = head  # Current node starts at the head

        # Traverse the list
        while curr is not None:
            next_node = curr.next  # Save the next node
            
            curr.next = prev  # Reverse the link
            
            # Move pointers forward
            prev = curr  # Move prev to the current node
            curr = next_node  # Move curr to the next node

        # prev is now the new head of the reversed list
        return prev


def print_list(node):
    while node is not None:
        print(f" {node.data}", end='')
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked List:", end='')
    print_list(head)

    head = reverseList(head)

    print("\nReversed Linked List:", end='')
    print_list(head)

