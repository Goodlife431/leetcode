class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

class solution(object):
    def is_palindrome(head):
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
