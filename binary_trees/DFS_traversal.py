# Inorder Traversal O(n)

def Inorder(root):

    if not root:
        return

    if root.left:
        Inorder(root.left)
    print(root.val)

    if root.right:
        Inorder(root.left)


# Preorder traversal

def Preorder(root):
    if not root:
        return
    
    print(root.val)

    if root.left:
        Preorder(root.left)
    if root.right:
        Preorder(root.right)


# PostOrder Traversal

def Postorder(root):

    if not root:
        return 
    
    if root.left:
        return Postorder(root.left)
    if root.right:
        return Postorder(root.right)
    
    print(root.val)

    
    