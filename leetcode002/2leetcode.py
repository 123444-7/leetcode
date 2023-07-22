"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if isinstance(l1, list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        if not l1:  # 若l1为空，直接返回l2
            return l2
        if not l2:  # 若l2为空，直接返回l1
            return l1

        l1.val += l2.val  # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:  # 若值大于等于10，则下一位自增1，并自身自减10
            l1.next = self.addTwoNumbers(ListNode(1), l1.next)
            l1.val -= 10

        l1.next = self.addTwoNumbers(l1.next, l2.next)  # 递归相加
        return l1

        # if len(l1) >= len(l2):
        #     short_list = l2
        #     long_list = l1
        # else:
        #     short_list = l1
        #     long_list = l2
        # output_list = []
        # for i in range(len(short_list)):
        #     num = long_list[i] + short_list[i]
        #     if num >= 10:
        #         num -= 10
        #         if i + 1 < len(long_list):
        #             long_list[i + 1] += 1
        #             output_list.append(num)
        #         else:
        #             output_list.append(0)
        #             output_list.append(1)
        # for i in range(len(short_list), len(long_list)):
        #     num = long_list[i]
        #     if num >= 10:
        #         num -= 10
        #         if i + 1 < len(long_list):
        #             long_list[i + 1] += 1
        #             output_list.append(num)
        #         else:
        #             output_list.append(0)
        #             output_list.append(1)
        #     else:
        #         output_list.append(long_list[i])
        # return output_list


a = Solution()
result = Solution.addTwoNumbers(a, l1=[8, 8, 8], l2=[2, 1, 1])
print(result)
