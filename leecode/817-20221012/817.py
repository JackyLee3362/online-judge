# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_nodes(self):
        """
        打印该结点之后的值（包括该结点）
        """
        while self:
            print(self.val)
            self = self.next

    def build_link_list(self, nums):
        """
        给定一组列表，创建一个带有头结点的链表
        nums: 长度为n的列表
        """
        n = len(head_list)
        for i in range(n):
            if i == 0:
                head.val = head_list[0]
                node = head
            else:
                next_node = ListNode(head_list[i], None)
                node.next = next_node
                node = next_node


List = list


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        node = head
        cnt, flag = 0, 0
        while node:
            if node.val in nums:
                flag = 1
            else:
                if flag == 1:
                    cnt += 1
                    flag = 0
            node = node.next
        return cnt + flag


solution = Solution()
head = ListNode()
head_list, num = [0, 1, 2, 3], [0, 1, 3]
head_list, num = [0, 1, 2], [0, 2]
head_list, num = [0], [0]
head.build_link_list(head_list)
# head.print_nodes()
print("solution is", solution.numComponents(head, num))
