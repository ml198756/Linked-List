# 交换链表中相邻节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点，它的 next 指向实际的头节点
        dummy = ListNode(-1)
        dummy.next = head
        
        # prev 指针始终指向要交换节点对的前一个节点
        prev = dummy
        
        # 进行节点交换，直到链表结束或者剩下单个节点
        while prev.next and prev.next.next:
            # current 指向第一个要交换的节点
            current = prev.next
            # next 指向第二个要交换的节点
            next = current.next
            
            # 交换 current 和 next
            current.next = next.next
            next.next = current
            prev.next = next
            
            # 移动 prev 指针到下一对要交换的节点的前一个位置
            prev = current
        
        # 返回虚拟头节点的 next，即新的头节点
        return dummy.next
