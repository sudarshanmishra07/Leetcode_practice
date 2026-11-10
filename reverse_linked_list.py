class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None                 #stores the previous node
        curr = head                 #start from the first node
        while curr:                 #traverse until end of linked list
            next_node = curr.next   #save next node
            curr.next = prev        #reverse current node link
            prev = curr             #move prev to current node
            curr = next_node        #move curr to next node 
        return prev