# Given a Binary Tree, complete the function to populate the next pointer for all nodes. The next pointer for every node should point to the Inorder successor of the node.
# You do not have to return or print anything. Just make changes in the root node given to you.

# Note: The node having no in-order successor will be pointed to -1. You don't have to add -1 explicitly, the driver code will take care of this.

# Examples :

# Input:
#        10
#        /  \
#       8   12
#      /
#     3
# Output: 3->8 8->10 10->12 12->-1
# Explanation: The inorder of the above tree is : 3 8 10 12. So the next pointer of node 3 is pointing to 8 , next pointer of 8 is pointing to 10 and so on.And next pointer of 12 is pointing to -1 as there is no inorder successor of 12.

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def populateNext(self, root):
        def inorder(node):
            nonlocal prev
            if not node:
                return
            
            inorder(node.left)
            
            if prev is not None:
                prev.next = node
            
            prev = node
            
            inorder(node.right)
        
        prev = None
        
        inorder(root)