# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        pre = None
        nex = None
        tmp = head
        index = 0
        o_head = None
        o_tail = None
        while index < m-1:
            pre = tmp
            tmp = tmp.next
            index = index+1
        
        o_head = tmp
        o_tail = tmp
        
        while index < n:
            nex = tmp.next
            tmp.next = o_head
            o_head = tmp
            tmp = nex
            index = index+1
        if pre:
            pre.next = o_head
        else:
            head = o_head
        o_tail.next = nex
        
        return head