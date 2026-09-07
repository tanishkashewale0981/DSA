class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree recursively
def create_tree():
    data = int(input("Enter data (-1 for no node): "))

    if data == -1:
        return None

    root = Node(data)

    print("Enter left child of", data)
    root.left = create_tree()

    print("Enter right child of", data)
    root.right = create_tree()

    return root


# Inorder: Left -> Root -> Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main program
root = create_tree()

print("\nInorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)



