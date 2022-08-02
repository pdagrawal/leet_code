class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        count = 1
        while head.next != None:
            count += 1
            head = head.next
        middle_index = int((count if count % 2 == 0 else count - 1)/2)
        for i in range(middle_index+1):
            if i == middle_index:
                return start
            else:
                start = start.next
