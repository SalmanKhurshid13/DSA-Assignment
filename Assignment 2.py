class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None
    
    # Create nodes
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

# Link nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = second  # cycle starts at node 2

# Test
sol = Solution()
result = sol.detectCycle(head)

if result:
    print("Cycle starts at node:", result.val)
else:
    print("No cycle")