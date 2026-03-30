app1 : {key idea is to add all the elements in a heap of size k and let heap handle the comparisons becuase k comparisons by own is bullshit.

now the concern is how to add all the elements into the heap.}

app1 --> bullshitted by neetcode solution their solution is even worse idk why this was not accepted.

app2 --> watched solution and code both, didnt liked this problem anyway still havent got any clue just trying to write the code which i saw basically copy pasting it

app2: {take two list from array lists and merge them using a helper function


'''python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeList(l1, l2))

            lists = merged_lists

        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        p1, p2 = l1, l2

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next

        if p1:
            curr.next = p1
        if p2:
            curr.next = p2

        return dummy.next




            






