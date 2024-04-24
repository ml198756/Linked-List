# 环形链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head
        has_cycle = False

        # 第一步：使用快慢指针检测环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        # 如果有环，找到环的入口
        if has_cycle:
            slow = head  # 将slow指针重置到头节点
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # 当slow和fast再次相遇时，就是环的起始节点

        return None  # 如果没有环，返回None
