# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous 
            previous = current
            current = next_node 
        
        return previous 