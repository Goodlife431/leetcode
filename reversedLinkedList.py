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