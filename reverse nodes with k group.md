# README

key idea is to add all the elements in a heap of size k and let heap handle the comparisons becuase k comparisons by own is bullshit.
app1 : {key idea is to add all the elements in a heap of size k and let heap handle the comparisons becuase k comparisons by own is bullshit.

now the concern is how to add all the elements into the heap.}

app1 --> bullshitted by neetcode solution their solution is even worse idk why this was not accepted.

app2 --> watched solution and code both, didnt liked this problem anyway still havent got any clue just trying to write the code which i saw basically copy pasting it

app2: {take two list from array lists and merge them using a helper function

now the concern is how to add all the elements into the heap.

```python
Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
self.next = next

class Solution(object):
    # make a helper function
    def getkth(self,curr,k): #start from dummy/GroupPrev
        while curr and k>0:
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
