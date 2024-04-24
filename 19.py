# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，它的 next 指向真正的头节点
        dummy = ListNode(0, head)
        
        # 初始化两个指针，都开始于虚拟头节点
        first = dummy
        second = dummy
        
        # 移动 first 指针，使得 first 和 second 之间的间隔是 n
        for _ in range(n + 1):  # 加一是因为我们希望 first 比 second 超前 n 个节点，包括虚拟头节点
            first = first.next
        
        # 移动两个指针，直到 first 指向链表的末尾
        while first is not None:
            first = first.next
            second = second.next
        
        # second 指针现在指向要删除节点的前一个节点
        # 删除 second.next 即倒数第 n 个节点
        second.next = second.next.next
        
        # 返回修改后的链表的头节点，即 dummy.next
        return dummy.next
