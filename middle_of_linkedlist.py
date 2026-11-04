class Solution:
    def getMiddle(self, head):
            slowptr = head
            fastptr = head
            #traverse the linked list using two pointers
            while fastptr is not None and fastptr.next is not None:
                fastptr = fastptr.next.next         #move fast pointer two step ahead
                slowptr = slowptr.next              #move slow pointer one step ahead
            return slowptr.data                     #return middle node data
