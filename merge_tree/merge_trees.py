
 
# input :
# t1 :
#     10
#   5    15
# 1


# t2 :
#     10
#        15
#           17
        
#         10 
#       5    15
#     1        17
          
#  output :
# t3 :
#     10
#   5    15
# 1        17

def merge_trees(root1,root2,root3):
    if root1 == None and root2 == None:
        //root3
        return 0
    elif root1 !=None and root2!= None:
        if root1.value==root2.value:
            root3.value =  root1.value
            root3.left = createNode()
            root3.right = createNode()
            l = merge_trees(root1.left,root2.left,root3.left)
            r = merge_trees(root1.right,root2.right,root3.right)
            if l==-1 or r== -1:
                return -1
        else:
            return -1
    elif root1==None and root2 != None:
            root3.value = root2.value
            root3.left = createNode()
            root3.right = createNode()
            l = merge_trees(root1,root2.left,root3.left)
            r = merge_trees(root1,root2.right,root3.right)
            if l==-1 or r== -1:
                return -1
    elif root1!=None and root2 == None:
            root3.value = root1.value
            root3.left = createNode()
            root3.right = createNode()
            l = merge_trees(root1.left,root2,root3.left)
            r = merge_trees(root1.right,root2,root3.right)
            if l==-1 or r== -1:
                return -1
    return 0
                   
          
