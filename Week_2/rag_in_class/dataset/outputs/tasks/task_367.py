class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    height_difference = abs(left_height - right_height)
    left_balanced = is_tree_balanced(root.left)
    right_balanced = is_tree_balanced(root.right)

    return (height_difference <= 1) and left_balanced and right_balanced
