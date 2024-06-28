# Backtracking is used to determine the path out of all the possible paths which satisfies a given condition.

def canReach(root):

    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True

    if canReach(root.left):
        return True
    if canReach(root.right):
        return True
    
    return False 

# Special Case

def leafPath(root,path):

    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and root.right:
        return True
    if leafPath(root.left,path):
        return True
    if leafPath(root.right):
        return True
    path.pop()

    return False 


