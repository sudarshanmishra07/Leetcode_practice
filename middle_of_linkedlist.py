class Solution:
    def getMiddle(self, head):
            slowptr = head
            fastptr = head
            while fastptr is not None and fastptr.next is not None:
                fastptr = fastptr.next.next
                slowptr = slowptr.next
            return slowptr.data
