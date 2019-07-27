# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def calc_zigzag( ltr_flag, parent_list, out):
    if len(parent_list):
        current_list = []
        parent_list.reverse()
        if ltr_flag:
            for node in parent_list:
                if node.left != None:
                    current_list.append(node.left)
                if node.right != None:
                    current_list.append(node.right)
        else:
            for node in parent_list:
                if node.right != None:
                    current_list.append(node.right)
                if node.left != None:
                    current_list.append(node.left)

        if len(current_list):
            out.append([x.val for x in current_list])
            calc_zigzag(not ltr_flag, current_list, out)

class Solution(object):

    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        left_to_right = True
        current_list = [root]
        out = []
        out.append([root.val])
        calc_zigzag( not left_to_right, current_list, out)
        return out
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

