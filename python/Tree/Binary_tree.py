class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# ALWAYS RETURN ROOT FOR THE OPERATION OF NEXT FUNCTION

# RECURSIVE PREOREDER TRAVERSAL
def preorder_rec(root):
    if root == None:
        return
    print(root.data)
    preorder_rec(root.left)
    preorder_rec(root.right)
    # Time Complexity: O(n). Space Complexity: O(n).


# RECURSIVE InOREDER TRAVERSAL
def inorder_rec(root):
    if root == None:
        return
    inorder_rec(root.left)
    print(root.data)
    inorder_rec(root.right)
    # Time Complexity: O(n). Space Complexity: O(n).


# RECURSIVE PostOREDER TRAVERSAL
def post_rec(root):
    if root == None:
        return
    post_rec(root.left)
    post_rec(root.right)
    print(root.data)
    # Time Complexity: O(n). Space Complexity: O(n).


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
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def level_order_line_by_line(root):
    if root == None:
        return "EMPTY BINARY TREE"
    queue = []
    queue.append(root)
    while queue:
        count = len(queue)
        result = []
        while count > 0:
            node = queue.pop(0)
            result.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            count -= 1
        print(result)


def findMax(root):

    # Base case
    if root == None:
        return 0

    # Return maximum of 3 values:
    # 1) Root's data
    # 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def find_min_in_BT(root):
    if root is None:
        return float("inf")
    res = root.data
    lres = find_min_in_BT(root.left)
    rres = find_min_in_BT(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def find_max_level(root):
    if root == None:
        return

    queue = []
    max = 0
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if max < node.data:
            max = node.data

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return max
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def find_min_level(root):
    if root == None:
        return

    queue = []
    min = float("inf")
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if min > node.data:
            min = node.data

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return min
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def search(root, data):
    if root == None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if node.data == data:
            return True
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return False
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def size(root):
    if root == None:
        return 0

    queue = []
    queue.append(root)
    # INITIALIZE COUNT WITH 0
    count = 0
    while len(queue) > 0:
        count = count + 1
        node = queue.pop(0)

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return count
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def insert(root, data):
    if root == None:
        newNode = Node(data)
        return root

    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        if node.left != None:
            queue.append(node.left)
        else:
            newNode = Node(data)
            node.left = newNode
            return root

        if node.right != None:
            queue.append(node.right)
        else:
            newNode = Node(data)
            node.left = newNode
            return root
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def reverseLevelOrder(root):
    S = []
    Q = []
    Q.append(root)

    # SIMILAR AS LEVEL ORDER TRAVERSAL BUT HERE ROOT"S RIGHT CHILD IS APPENDED FIRST

    while len(Q) > 0:

        root = Q.pop(0)
        S.append(root.data)

        if root.right:
            Q.append(root.right)

        if root.left:
            Q.append(root.left)
    print("S", S)
    S = S[::-1]
    for i in S:
        print(i)
    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


def delete_binary_tree(root):
    if root == None:
        return
    delete_binary_tree(root.left)
    delete_binary_tree(root.right)
    print("DELETING NODE DATA", root.data)
    root = None

    # Time Complexity: O(n) where n is number of nodes in the binary tree
    # Space Complexity: O(n) where n is number of nodes in the binary tree


# FUNCTION TO FIND THE HEIGHT OF THE BINARY TREE
# 1. If tree is empty then return 0
# 2. Else
#      (a) Get the max depth of left subtree recursively  i.e.,
#           call maxDepth( tree->left-subtree)
#      (a) Get the max depth of right subtree recursively  i.e.,
#           call maxDepth( tree->right-subtree)
#      (c) Get the max of max depths of left and right
#           subtrees and add 1 to it for the current node.
#          max_depth = max(max dept of left subtree,
#                              max depth of right subtree)
#                              + 1
#      (d) Return max_depth
def maxDepth(node):  # HEIGHT
    if node is None:
        return 0

    else:

        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        return max(lDepth, rDepth) + 1
# Time Complexity: O(n)


def maxwidth(root):
    if root == None:
        return 0
    queue = []
    queue.append(root)

    max_width = 0

    while len(queue) != 0:
        count = len(queue)
        max_width = max(count, max_width)

        while count > 0:
            node = queue.pop(0)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            count = count-1
    return max_width
    # Time Complexity: O(n)
    # Space Complexity: O(n)


def levelsum(root):
    if root == None:
        return 0
    queue = []
    queue.append(root)
    while len(queue) != 0:
        count = len(queue)
        lsum = []
        while count > 0:
            node = queue.pop(0)
            lsum.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            count = count-1
        print(sum(lsum))
    # Time Complexity: O(n)
    # Space Complexity: O(n)


def printRoute(stack, root):
    if root == None:
        return None

    # append this node to the path array
    stack.append(root.data)
    if root.left == None and root.right == None:

        # print out all of its
        # root - to - leaf
        print(" ".join([str(i) for i in stack]))

    # otherwise try both subtrees
    printRoute(stack, root.left)
    printRoute(stack, root.right)
    stack.pop()


s = 0


def sumpath(stack, root):
    if root == None:
        return
    global s
    # append this node to the path array
    stack.append(root.data)
    if root.left == None and root.right == None:
        s = s + int("".join([str(i) for i in stack]))
        print("SUM OF ALL NODE DATA IN PATH", sum(stack))

    sumpath(stack, root.left)
    sumpath(stack, root.right)
    stack.pop()


def sumofallelements(root):
    if root == None:
        return None

    queue = []
    result = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.left:
            queue.append(node.right)

    print("SUM OF ALL ELEMENTS", sum(result))


def noofleaves(root):
    if root == None:
        return "EMPTY BINARY TREE"
    queue = []
    queue.append(root)
    count = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left == None and node.right == None:
            count = count + 1
        else:
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
    print(count)


def noofullnode(root):
    if root == None:
        return "EMPTY BINARY TREE"
    queue = []
    queue.append(root)
    count = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left != None and node.right != None:
            count = count + 1
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    print(count)


def delete_data(root, data):
    if root == None:
        return None

    queue = []
    result = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)
        if node.data == data:
            node1 = node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    dep = result.pop()
    node1.data = dep
    queue = []
    queue.append(root)
    print("DATA", node.data)

    while len(queue) > 0:
        node2 = queue.pop(0)
        if node2 == node:
            node2 = None
        if node2.left == node:
            node2.left = None
            break
        else:
            queue.append(node2.left)
        if node2.right == node:
            node2.right = None
            break
        else:
            queue.append(node2.right)
    return root


def mirror(root):
    if root == None:
        return None

    queue = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        temp = node.right
        node.right = node.left
        node.left = temp

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)

    return root


def zigzagtraversal(root):

    # Base Case
    if root is None:
        return

    # Create two stacks to store current
    # and next level
    currentLevel = []
    nextLevel = []

    # if ltr is true push nodes from
    # left to right otherwise from
    # right to left
    ltr = True

    # append root to currentlevel stack
    currentLevel.append(root)

    # Check if stack is empty
    while len(currentLevel) > 0:
        # pop from stack
        temp = currentLevel.pop(-1)
        # print the data
        print(temp.data, " ", end="")

        if ltr:
            # if ltr is true push left
            # before right
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            # reverse ltr to push node in
            # opposite order
            ltr = not ltr
            # swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel


def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.data == n1 or root.data == n2:
        return root

    # Look for datas in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one data
    # is present in one subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca
    # The method 1 finds LCA in O(n) time


def printAncestors(root, target):

    # Base case
    if root == None:
        return False
    print("d", root.data)
    if root.data == target:
        return True

    # If target is present in either left or right subtree
    # of this node, then print this node
    if printAncestors(root.left, target) or printAncestors(root.right, target):
        print(root.data)
        return True

    # Else return False
    return False


hashTable = {}


def verticalsum(root, column):
    if not root:
        return None

    if column not in hashTable:
        hashTable[column] = 0
    hashTable[column] = hashTable[column] + root.data
    verticalsum(root.left, column - 1)
    verticalsum(root.right, column + 1)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # preorder_rec(root)
    # inorder_rec(root)
    # post_rec(root)
    level_order(root)
    # level_order_line_by_line(root)
    # print("Maximum element is", findMax(root))
    # print("Minimum element is", find_min_in_BT(root))
    # print("Maximum element is", find_max_level(root))
    # print("Minimum element is", find_min_level(root))
    # print(search(root, 11))
    # root = insert(root, 9)
    # level_order(root)
    # print(size(root))
    # reverseLevelOrder(root)
    # delete_binary_tree(root)
    # print(maxDepth(root))
    root = delete_data(root, 5)
    # noofleaves(root)
    # noofullnode(root)
    level_order(root)
    # print(maxwidth(root))
    # levelsum(root)
    # printRoute([], root)
    # sumpath([], root)
    # print(s)
    # sumofallelements(root)
    # root = mirror(root)
    # level_order(root)
    # print(findLCA(root, 4, 5).data)
    # printAncestors(root, 7)
    # zigzagtraversal(root)
    # verticalsum(root, 0)
    # print(hashTable)
