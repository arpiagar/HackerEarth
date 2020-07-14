class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count =0
        node_map = {}
        def helper(node, node_map):
            
            if not node.left and not node.right:
                self.count += 1
                node_map[self.count] = node
                return 
            if node.left:
                helper(node.left, node_map)
            self.count += 1
            node_map[self.count] = node
            if node.right:
                helper(node.right, node_map)
        if not root:
            return -1
        helper(root, node_map)
        
        if k not in node_map:
            return -1
        return node_map[k].val
