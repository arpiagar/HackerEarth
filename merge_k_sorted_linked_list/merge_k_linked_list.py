class Node:
    def __init__(self, value):
        self.value =  value
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head =  None

    def create(self,input_list):
        flag =  True
        for elem in input_list:
            if self.head ==  None:
                self.head =  Node(elem)
            else:
                if flag:
                    self.head.next =  Node(elem)
                    flag =  False
                    temp = self.head.next
                else:
                    temp.next = Node(elem)
                    temp = temp.next
        return self.head

    def print_list(self):
        temp = self.head
        while temp.next != None:
            print temp.value
            temp = temp.next


def get_minimum(header_list):
  minimum = None
  minimum_idx = -1
  for i in  xrange(0,len(header_list)):
    node = header_list[i]
    if node != None:
      if minimum == None:
        minimum = node.value
        minimum_idx = i
      else:
        if node.value < minimum:
          minimum = node.value
          minimum_idx = i
  return minimum,minimum_idx

      
  

def mergeK(input_list):
    k = len(input_list)
    new_list = []
    while True:
        minimum, minimum_idx = get_minimum(input_list)
        if minimum_idx == -1 or minimum == None:
            break
        else:
            new_list.append(minimum)
            input_list[minimum_idx] = input_list[minimum_idx].next
    print new_list
        


if __name__ == '__main__':
    ll1  = LinkedList()
    ll1.create([1,12,23,34,45,56])
    ll2  = LinkedList()
    ll2.create([55,66,67,89,91])
    ll3  = LinkedList()
    ll3.create([2,3,4,5,6,7])
    input_list =  [ll1.head,ll2.head,ll3.head]
    mergeK(input_list)

