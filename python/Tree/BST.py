from math import ceil


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class DLLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None


def search(root, data):
    if root == None:
        print("EMPTY TREE")
        return

    current = root

    while current != None:
        if current.data == data:
            print("FOUND")
            return True
        if data > current.data:
            current = current.right
        else:
            current = current.left

    return False

# Time Complexity(min): O(logn) in case of BST since it depends upon height of BST
# Time Complexity: O(n), in worst case (when BST is a skew tree). Space Complexity: O(n), for recursive stack.


def minelement(root):
    if root == None:
        print("EMPTY TREE")
        return

    current = root

    while current.left != None:
        current = current.left

    print("MIN ELEMENT", current.data)
    return current
    # Time Complexity: O(n), in worst case (when BST is a left skew tree).
    # S(n)=O(n)


def maxelement(root):
    if root == None:
        print("EMPTY TREE")
        return

    current = root

    while current.right != None:
        current = current.right

    print("Max ELEMENT", current.data)
    # Time Complexity: O(n), in worst case (when BST is a left skew tree).
    # S(n)=O(n)


def inorderpred(root, node):
    current = node.left
    while current.right != None:
        current = current.right

    print("INORDER PREDECESSOR", current.data)


def inordersucc(root, node):
    current = node.right
    while current.left != None:
        current = current.left

    print("INORDER SUCCESSOR", current.data)


def insertnode(root, data):
    if root == None:
        root = Node(data)
        return

    if data > root.data:
        if root.right == None:
            root.right = Node(data)
            return
        else:
            insertnode(root.right, data)
    else:
        if root.left == None:
            root.left = Node(data)
            return
        else:
            insertnode(root.left, data)
    # Time Complexity:O(n). Space Complcxity:O(n) for recursive stack.


def inordertraversal(root):
    if root == None:
        return
    inordertraversal(root.left)
    print(root.data)
    result.append(root.data)
    inordertraversal(root.right)
    return result


def delete_bst(root):
    if root == None:
        return
    delete_bst(root.left)
    delete_bst(root.right)
    print("DELETING NODE DATA", root.data)
    root = None

# def BSTingivenrange(root):


def lca(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root
    # The Time Complexity of the above solution is O(h), where h is the height of the tree.


def distancebetwennode(root, n1, n2):
    if root == None:
        return 0
    if root.data > n1 and root.data > n2:
        return distancebetwennode(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return distancebetwennode(root.right, n1, n2)
    else:
        return distanceFromRoot(root, n1) + distanceFromRoot(root, n2)


def distanceFromRoot(root, x):
    if root.data == x:
        return 0
    count = 0
    current = root
    while current != None:
        if current.data == x:
            print("DISTANCE FROM ROOT", count)
            break
        if current.data < x:
            current = current.right
        else:
            current = current.left
        count = count + 1
    return count


result = []


def deleteNode(root, key):

    # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minelement(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root
# Time Complexity: The worst case time complexity of delete operation is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of delete operation may become O(n)


def isBST(root):
    global result
    if root == None:
        return None
    isBST(root.left)
    print(root.data)
    result.append(root.data)
    isBST(root.right)


def sortedArrayToBST(arr):

    if not arr:
        return None

    # find middle
    mid = int((len(arr) / 2))

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root
# Time Complexity: O(n)
# Following is the recurrance relation for sortedArrayToBST().

#   T(n) = 2T(n/2) + C
#   T(n) -->  Time taken for an array of size n
#    C   -->  Constant (Finding middle of array and linking root to left
#                       and right subtrees take constant time)


def BSTtoCLL(root, a):
    l = inordertraversal(root)
    print(l)
    CLL = DLL()
    CLL.head = DLLNode(l.pop(0))
    current = CLL.head
    while len(l) > 0:
        newnode = DLLNode(l.pop(0))
        current.next = newnode
        current = current.next
    current.next = CLL.head
    current = CLL.head
    while True:
        print(current.data)
        current = current.next
        if current == CLL.head:
            break


def height(node):  # HEIGHT
    if node is None:
        return 0

    else:

        lDepth = height(node.left)
        rDepth = height(node.right)

        return max(lDepth, rDepth) + 1


def isBalanced(root):

    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True

    # if we reach here means tree is not
    # height-balanced tree
    return False
# Time Complexity: O(n^2) Worst case occurs in case of skewed tree.
# Delete leaf nodes from binary search tree.


def leafDelete(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None

    # Else recursively delete in left
    # and right subtrees.
    root.left = leafDelete(root.left)
    root.right = leafDelete(root.right)

    return root


# There are two possible cases for every node.
# 1) Node’s key is outside the given range. This case has two sub-cases.
# …….a) Node’s key is smaller than the min value.
# …….b) Node’s key is greater that the max value.
# 2) Node’s key is in range.
# We don’t need to do anything for case 2. In case 1, we need to remove the node and change root of sub-tree rooted with this node.
# The idea is to fix the tree in Postorder fashion.
# When we visit a node, we make sure that its left and right sub-trees are already fixed.
#  In case 1.a), we simply remove root and return right sub-tree as new root.
# In case 1.b), we remove root and return left sub-tree as new root.
def removeOutsideRange(root, Min, Max):

    # Base Case
    if root == None:
        return None

    # First fix the left and right
    # subtrees of root
    root.left = removeOutsideRange(root.left,
                                   Min, Max)
    root.right = removeOutsideRange(root.right,
                                    Min, Max)

    # Now fix the root. There are 2
    # possible cases for toot
    # 1.a) Root's key is smaller than
    #      min value (root is not in range)
    if root.key < Min:
        rChild = root.right
        return rChild

    # 1.b) Root's key is greater than max
    #      value (root is not in range)
    if root.key > Max:
        lChild = root.left
        return lChild

    # 2. Root is in range
    return root


# Time Complexity: O(n) where n is the number of nodes in given BST.


# ITS FOR A NORMAL BINARY TREE
def RemoveHalfNodes(root):
    if root is None:
        return None

    # Recur to left tree
    root.left = RemoveHalfNodes(root.left)

    # Recur to right tree
    root.right = RemoveHalfNodes(root.right)

    # if both left and right child is None
    # the node is not a Half node
    if root.left is None and root.right is None:
        return root

    # If current nodes is a half node with left child
    # None then it's right child is returned and
    # replaces it in the given tree
    if root.left is None:
        new_root = root.right
        temp = root
        root = None
        del(temp)
        return new_root

    if root.right is None:
        new_root = root.left
        temp = root
        root = None
        del(temp)
        return new_root

    return root
# Time complexity of the above solution is O(n) as it does a simple traversal of binary tree.


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    root = leafDelete(root)
    # search(root, 11)
    # minelement(root)
    # maxelement(root)
    # inorderpred(root, root)
    # inordersucc(root, root)
    # # insertnode(root, 11)
    inordertraversal(root)
    # print(lca(root, 8, 6).data)
    # # distanceFromRoot(root, 9)
    # print("DISTANCE BETWEEN TWO NODES",distancesbetwennode(root,1,3))
    # isBST(root)
    # if result == sorted(result):
    #     print("BST")
    # else:
    #     print("NO BST")
    # list = [1, 2, 3, 4, 5, 6, 7, 8]
    # root = sortedArrayToBST(list)
    # inordertraversal(root)
    # BSTtoCLL(root)
