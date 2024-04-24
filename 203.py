
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，这样可以方便处理头节点就是目标值的情况
        dummy = ListNode(-1)
        dummy.next = head
        
        # previous 指向当前节点的前一个节点
        previous = dummy
        
        # 遍历链表
        while head:
            if head.val == val:
                # 跳过当前节点，删除它
                previous.next = head.next
            else:
                # 移动previous指针到当前节点
                previous = head
            # 移动head指针到下一个节点
            head = head.next
        
        # 返回虚拟头节点的下一个节点，即新的头节点
        return dummy.next
