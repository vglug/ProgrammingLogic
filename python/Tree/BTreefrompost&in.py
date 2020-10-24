''' 
The idea is to start with the root node which would be the last item in the postorder sequence and find boundary of its left and right subtree in the inorder sequence. 
To find the boundary, we search for index of the root node in inorder sequence. Now all keys before the root node in inorder sequence becomes part of the left subtree and all keys after the root node becomes part of the right subtree. 
We repeat this recursively for all nodes in the tree, and construct the tree in the process.'''


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order(root):
    if root == None:
        return "EMPTY BINARY TREE"
    queue = []
    result = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)

    for i in result:
        print(i)


# FROM PREORDER & INORDER
def construct1(pre, ino):
    if ino:
        root = Node(pre.pop(0))
        root_index = ino.index(int(root.data))
        root.left = construct1(pre, ino[:root_index])
        root.right = construct1(pre, ino[root_index + 1:])
        return root


if __name__ == "__main__":
    root = construct1([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    level_order(root)
