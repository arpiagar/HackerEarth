#https://leetcode.com/problems/diameter-of-binary-tree/submissions/


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        return self.diameter(root, 0)[1]


    def diameter(self, node, max_val):
        if not node:
            return 0, max_val ##NUll node
        left = right = 0
        if node.left == None and node.right == None:
            return 1, max(max_val, 1)  #Leaf node
        if node.left != None:
            left, max_val  = self.diameter(node.left, max_val)
        if node.right != None:
            right, max_val  = self.diameter(node.right, max_val)
        print(left, right, max_val)
        return max(left,right)+1, max(max_val ,left+right)
