# README


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # make a helper function
    def getkth(self,curr,k): #start from dummy/GroupPrev
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr #this will give return the kth node
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)

        GroupPrev = dummy

        while True:
            kth = self.getkth(GroupPrev,k)
            if not kth:
                break
            GroupNext = kth.next

            #start reversing 
            curr = GroupPrev.next
            prev = kth.next
            while curr!= GroupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                # temp.next = curr
                curr = temp
            tmp1 = GroupPrev.next 
            #the groupprev.next is pointing at that node which which was the starting node before rever
            #sal and the node before next group after reversal in first case it is 1
            #so basically dummy.next on which GroupPrev was there before will be pointing 
            #at the new head of list 

            GroupPrev.next = kth
            GroupPrev = tmp1
            # GroupPrev = kth.next
            # GroupPrev = curr

        return dummy.next


