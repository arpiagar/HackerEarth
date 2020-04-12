#https://leetcode.com/problems/binary-search-tree-iterator/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 7 3
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node_list = [root]
        self.node_visited = {root: 0}

    def next(self) -> int:
        """
        @return the next smallest number
        """

        return self.add_to_list_and_map().val

    def add_to_list_and_map(self):
        node = self.node_list[0]
        temp_node = node
        if self.node_visited[temp_node] == 0:
            self.node_visited[temp_node]  = 1
            if temp_node.left:
                while temp_node.left !=None:
                    self.node_list.append(temp_node.left)
                    self.node_visited[temp_node.left] = 1
                    temp_node=temp_node.left
                self.node_visited[temp_node] = 2
                return temp_node
            else:
                self.node_visited[temp_node] = 1
                return self.add_to_list_and_map()
        elif self.node_visited[node] == 1:
            self.node_visited[node] = 2
            return node
        else:
            self.node_list = self.node_list[1:]
            if node.right == None:
                return self.add_to_list_and_map()
            else:
                self.node_list.append(node.right)
                self.node_visited[node.right]=0
                return self.add_to_list_and_map()



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.node_list:
            print(len(self.node_list),self.node_list[0].left,self.node_list[0].right, self.node_list[0].val, self.node_visited[self.node_list[0]])
            if len(self.node_list) == 1 and self.node_visited[self.node_list[0]]==2 and not self.node_list[0].right:
                return False
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
