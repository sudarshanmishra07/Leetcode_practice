class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()          # Create a dummy node to start the merged list
        tail = dummy                # Tail keeps track of the last node in the merged list

        while list1 and list2:
            if list1.val<list2.val: 
                tail.next = list1   # Attach the current node of list1
                list1 = list1.next  # Move list1 to its next node
            else:
                tail.next = list2   # Attach the current node of list2
                list2 = list2.next  # Move list2 to its next node
            tail = tail.next
        if list1:
            tail.next = list1       # Attach the remaining nodes of list1, if any
        elif list2:
            tail.next = list2       # Otherwise, attach the remaining nodes of list2, if any
        dummy = ListNode()            # Create a dummy node to start the merged list
        tail = dummy                  # Tail keeps track of the last node in the merged list

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1     # Attach the current node of list1
                list1 = list1.next    # Move list1 to its next node
            else:
                tail.next = list2     # Attach the current node of list2
                list2 = list2.next    # Move list2 to its next node
            tail = tail.next
        if list1:
            tail.next = list1         # Attach the remaining nodes of list1, if any
        elif list2:
            tail.next = list2         # Otherwise, attach the remaining nodes of list2, if any
        
        return dummy.next
