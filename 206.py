# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表

# 双指针写法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_temp = current.next  # 保存当前节点的下一个节点
            current.next = prev       # 反转当前节点的指针
            prev = current            # 移动prev和current指针
            current = next_temp
        return prev  # prev变成了新的头节点

# 递归写法

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件，如果链表为空或者只有一个节点，直接返回
        if not head or not head.next:
            return head
        
        # 递归反转链表的剩余部分
        new_head = self.reverseList(head.next)
        
        # 将当前节点的下一个节点的 next 指向当前节点（反转链接）
        head.next.next = head
        # 将当前节点的 next 指向 None（避免循环链表）
        head.next = None
        
        # 返回反转后的链表的头节点
        return new_head
