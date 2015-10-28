#WAP to alternately reverse a linked list
# A->B->C->D
# B->A->D->C
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
       
def alternate_reverse(root):
    if root !=None and root.next!= None:
        temp = root.next.next
        next_node =  root.next
        root.next.next=root
        root.next = alternate_reverse(temp)
        return next_node
    else:
        return root
    
if __name__ == "__main__":
    head =  Node(5)
    head.next = Node(7)
    head.next.next =  Node(9)
    head.next.next.next =  Node(11)
    head.next.next.next.next =  Node(13)
    head = alternate_reverse(head)   
    print head.value
    print head.next.value
    print head.next.next.value
    print head.next.next.next.value
    print head.next.next.next.next.value
