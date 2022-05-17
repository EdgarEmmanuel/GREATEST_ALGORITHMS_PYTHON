from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"the val is {self.val} and the next {self.next}"


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
        return list

    def formatResultNow(self, list, head, index):
        EMPTY = 0
        if len(list) == EMPTY:
            return list
        else:
            current = head
            next = head.next
            previous = None
            list = []
            cpt = 0
            while next is not None:
                # print(current)
                list.append(current.val)
                if cpt == index:
                    #print("stop here")
                    #print(previous)
                    if current.next is not None:
                        previous.next = current.next
                    else:
                        previous.next = None
                    #print(current)
                    #print(previous)
                previous = current
                current = next
                next = next.next
                cpt += 1
            return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list = self.fromListNodeToList(head)
        newList = []
        indexOfItemToDelete = len(list) - n

        for index in range(len(list)):
            if index != indexOfItemToDelete:
                newList.append(list[index])

        #data = self.formatResultNow(newList, head, indexOfItemToDelete)
        #print(self.fromListNodeToList(data))
        return self.formatResultNow(newList, head, indexOfItemToDelete)


five = ListNode(5)
four = ListNode(4, five)
third = ListNode(3, four)
second = ListNode(2, third)
first = ListNode(1, second)

if __name__ == "__main__":
    response = Solution().removeNthFromEnd(first, 2)
    # response_two = Solution().removeNthFromEnd(ListNode(1),1)
