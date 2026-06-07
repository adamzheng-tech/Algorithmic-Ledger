# LeetCode Problem 2: Add two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Incorrect Compilation 1:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not list: # if not list, list?
            return 0
        
        num_1 = 0
        num_2 = 0

        for a in range(len(l1)):
            num_1 = num_1 + l1.val * 10 ** a
            l1. val = l1.next.val
        return num_1

        for b in range(len(l2)):
            num_2 = num_2 + l2.val * 10 ** b
            l2.val = l2.next.val
        return num_2

        num = num_1 + num_2
        l3 = []

        while num != 0:
            digit = num % 10
            l3 = digit
    
    # The current approach of converting list nodes to an integer, adding them, and converting back is 
    # a structural failure—it ignores the constraints of linked list manipulation. Implement a direct 
    # traversal using a carry variable to handle the addition of nodes in situ.

# Incorrect Compilation 2:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not list: # if not list, list?
            return []

        return_list = []
        return_list.val = dummy # The right way to allocate memory for a new node on the heap is using ListNode() constructor. 
        current = dummy
        
        while l1.next != None or l2.next != None or carry > 0: # The first nodes of l1 and l2 are bypassed.
            val1 = l1.val 
            val2 = l2.val # If l1 or l2 is None, the l1.val or l2.val will raise an AttributeError. They won't automatically return 0.
            val_sum = val1 + val2 + carry
            carry = val_sum // 10
            new_node = sum % 10
            current.next = new_node
            current = current.next
        
        return dummy.next 

# Incorrect Compilation 3:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: # Brackets?
            return []

        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0 # The while loop actually doesn't move the l1 and l2 pointers forward automatically.
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry
            carry = val_sum // 10
            new_node = ListNode(val_sum % 10)
            current.next = new_node
            current = current.next
        
        return dummy.next 

# Correction for the above 3:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: # Brackets?
            return []

        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry
            carry = val_sum // 10
            new_node = ListNode(val_sum % 10)
            current.next = new_node
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next 

# Miscompilation 4:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: # Brackets?
            return []

        dummy = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry
            carry = val_sum // 10
            new_node = ListNode(val_sum % 10)
            dummy.next = new_node # Does it save the memory space for "current"? Yes. But it also causes a linked list overwrite.

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next 