from typing import Optional

# list_1 = 1,2,4
# list_2 = 1,3,4

# 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)

        return head


leet_code = Solution()

list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)


result_1 = leet_code.mergeTwoLists(list_1, list_2) # Result 1,1,2,3,4,4
result_2 = leet_code.mergeTwoLists(None, None) # []
result_3 = leet_code.mergeTwoLists(None, ListNode(0)) # [0]

print(result_1)
print(result_2)
print(result_3)