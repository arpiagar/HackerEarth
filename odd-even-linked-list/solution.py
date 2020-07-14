class Solution:
    
    def oddEvenList(self, head: ListNode) -> ListNode:    
        if not head :
            return head
        temp = head
        counter=1
        
        if counter %2: 
            odd = temp # odd => 1 , temp => 1 
        counter += 1
        while(temp.next):
            n_node = temp.next # 2 
            if (counter % 2):  #o t n t.n
                if not odd:  #  1 2 3 4 5
                    temp.next = n_node.next
                    n_node.next = head
                    head = n_node
                    odd = head
                else:
                    temp.next = n_node.next
                    n_node.next = odd.next
                    odd.next = n_node
                    odd = n_node
            else:
                temp = temp.next
            counter += 1
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       # if you want to take the value in the list to determine odd even and
       # not the indices. 
    def oddEvenListValueBased(self, head: ListNode) -> ListNode:
        # 1 -> 2 -> 3 -> 4 ->5 
        # odd ptr, even ptr
        # 1 2 4 
        # 1 2 3
        # 1 3 2
        # 2 1 3
        # 2 4 1
        # 
        
        if not head :
            return head
        temp = head
        if temp.val %2: 
            odd = temp # odd => 1 , temp => 1 
        else:
            odd = None
        
        while(temp.next):
            n_node = temp.next # 2 
            if (n_node.val%2):  #o t n t.n
                if not odd:  #  1 2 3 4 5
                    temp.next = n_node.next
                    n_node.next = head
                    head = n_node
                    odd = head
                else:
                    temp.next = n_node.next
                    n_node.next = odd.next
                    odd.next = n_node
                    odd = n_node
            else:
                temp = temp.next
        return head
    
