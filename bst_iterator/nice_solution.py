class BSTIterator:

    def __init__(self, root: TreeNode):
        if root:
            self.visited_map = {}
            self.curr_node = root
            self.node_stack = [root]
        else:
            self.node_stack = []
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.find_node().val
        
        
    def find_node(self):
        if not self.node_stack:
            return None
        curr_node = self.node_stack[-1]
        if curr_node not in self.visited_map:
            if curr_node.left and curr_node.left not in self.visited_map:
                self.node_stack.append(curr_node.left)
                return self.find_node()
            else:
                self.node_stack.pop()
                self.visited_map[curr_node] = True
                if curr_node.right:
                    self.node_stack.append(curr_node.right)
                return curr_node

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.node_stack:
            return True
        else:
            return False
