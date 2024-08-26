class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(depth):
    if depth == 0:
        return None
    root = TreeNode(0)
    nodes = [root]
    for _ in range(depth - 1):
        new_nodes = []
        for node in nodes:
            node.left = TreeNode(0)
            node.right = TreeNode(1)
            new_nodes.extend([node.left, node.right])
        nodes = new_nodes
    return root

def find_path(root, binary_number):
    path = []
    current_node = root
    for digit in binary_number:
        if digit == '1':
            current_node = current_node.right
            path.append('Right')
        else:
            current_node = current_node.left
            path.append('Left')
    return path

def count_ones(binary_number):
    return binary_number.count('1')

def main():
    binary_number = '10111'
    if count_ones(binary_number) % 2 != 0:
        print("The binary number does not have an even number of 1s.")
        return

    tree_depth = 5
    root = build_tree(tree_depth)
    path = find_path(root, binary_number)
    print(f"The path to the leaf node {binary_number} is: {' -> '.join(path)}")

if __name__ == "__main__":
    main()
