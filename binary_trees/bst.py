# BST should have all the nodes in the lrft subtree smaller than the root and all the nodes in the right subtree greater than the root, this hold true for all teh nodes in the tree.

def search(root, target):

    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
    
# BST Insert a node O(logn)
class TreeNode:
    def __init__(self,val):
        self.val = val

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right,val)
    elif val < root.val:
        root.left = insert(root.left,val)
    else:
        return root


# BST Remove a Node O(logn)

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root,val):

    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right,val)
    elif val < root.val:
        root.left = remove(root.left,val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.right
        else:
            minNode = minValueNode(root.right)
            root.val = minNode
            root.right = remove(root.right,minValueNode)