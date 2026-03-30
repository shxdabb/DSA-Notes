app1 : {key idea is to add all the elements in a heap of size k and let heap handle the comparisons becuase k comparisons by own is bullshit.

now the concern is how to add all the elements into the heap.}

app1 --> bullshitted by neetcode solution their solution is even worse idk why this was not accepted.

app2 --> watched solution and code both, didnt liked this problem anyway still havent got any clue just trying to write the code which i saw basically copy pasting it

app2: {take two list from array lists and merge them using a helper function



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        
        #basically iterate through lists so u will be at [1,4,5] then [1,3,4]
        #take two list at a time and merge them 
        if not lists and len(lists)==0:
            return None
          
        
        while len(lists)>1: #iterate over lists
            mergedlists = []
            for i in range(0,len(lists),2): #we will merge them in pairs
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None #cuz l2 cant be there sometime 
                                                        #single shit

                mergedlists.append(self.mergelist(l1,l2))
            lists = mergedlists #doubt
        

        return lists[0]

            
    def mergelist(self,l1,l2):
        dummy = ListNode()
        curr = dummy
        p1,p2 = l1,l2
        while p1 and p2: # doubt wtf is l1 and l2 here the array of head 

            if p1.val <= p2.val:
                curr.next = p1    #[[1,4,5,6],[1,3,4]
                p1 = p1.next
                curr = curr.next  #d->1->2->3->4->4->5
            elif p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
                curr = curr.next

        if p1:
            curr.next = p1
                
        if p2:
            curr.next = p2
        return dummy.next


        my older approach
        # dummy = ListNode()
        # curr = dummy
        # heap = []

        # for heads in lists:
        #     #need a while loop to access all k elements
        #     heapq.heappush(heap,list[list[heads]])





            






