""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# traverse the tree in order
# returns the node value in an array
def in_order_traverse(root, arr=[]):
    if root.left: 
        in_order_traverse(root.left, arr)
    arr.append(root.data)
    if root.right:
        in_order_traverse(root.right, arr)

        

# return a boolean indicating whether the array is
# in sorted ascending order

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False 
    return True
    

def checkBST(root):
    # have a previous pointer that keeps track of the grandparent's value
    # push every tree node value into an array so that we can check previous generations
    
    # traverse through the tree
    # if there is a right but its value < its parent, then that's not valid
    # if there is a left but its value > its parent, then that's not valid
    # we might every well have to check past just a single generation
        # how do we do that?
        # we oculd keep traversing backwards up the tree to check earlier generations?
        
    tree_values = []
    # traverse the tree in-order, add the elements to an array 
    in_order_traverse(root, tree_values)
  
    # check that the elements are sorted 
    return is_sorted(tree_values)
