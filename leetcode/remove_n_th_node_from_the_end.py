from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"the val is {self.val} and the next {self.next.val}"


class Solution:
    def getTheLength(self, head: Optional[ListNode]) -> int:
        next = head.next
        cpt = 1
        while next is not None:
            next = next.next
            cpt += 1

        return cpt

    def fromListNodeToList(self, head):
        current = head
        next = head.next
        list = []

        while next is not None:
            list.append(current.val)
            current = next
            next = next.next

        list.append(current.val)
        #print(list)
        return list


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list = self.fromListNodeToList(head)
        indexOfItemToDelete = len(list) - n
        print(indexOfItemToDelete)

        for i in range(len(list)):
            print(list[i], i)


five = ListNode(5)
four = ListNode(4,five)
third = ListNode(3,four)
second = ListNode(2, third)
first = ListNode(1,second)

if __name__ == "__main__":
    response = Solution().removeNthFromEnd(first,2)
    #response_two = Solution().removeNthFromEnd(ListNode(1),1)