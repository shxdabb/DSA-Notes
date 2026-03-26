# README

```python
Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
self.next = next

class Solution(object):
    # make a helper function
    def getkth(self,curr,k): #start from dummy/GroupPrev
        while curr and k&gt;0:
            curr = curr.next
            k-=1
        return curr #this will give return the kth node

    def reverseKGroup(self, head, k):
    
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        
        dummy = ListNode(0,head)

        GroupPrev = dummy

        while True:
            kth = getkth(GroupPrev,k)
            if not kth:
                return GroupPrev
            GroupNext = kth.next

            #start reversing 
            curr = GroupPrev.next
            prev = GroupNext
            while curr!= GroupNext:
                temp = curr.next
                curr.next = prev
                # prev = curr
                temp.next = curr
                curr = temp
            # GroupPrev = kth.next
            GroupPrev = curr
        return GroupPrev
