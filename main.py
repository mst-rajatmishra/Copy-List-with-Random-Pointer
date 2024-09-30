class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create new nodes and insert them next to their original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set the random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the two lists
        original = head
        copy_head = head.next
        copy_current = copy_head
        
        while original:
            original.next = original.next.next  # Restore original list
            if copy_current.next:
                copy_current.next = copy_current.next.next  # Move to next copied node
            original = original.next
            copy_current = copy_current.next

        return copy_head
