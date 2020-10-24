class Node:
    def __init__(self, data=None):
        self.data = data
        self.childlist = []

    def addchildren(self, child):
        self.childlist.append(child)


def level_order(root):
    if root == None:
        return

    queue = []
    result = []

    queue.append(root)

    while len(queue) > 0:
        print("Q", result)
        node = queue.pop(0)
        result.append(node.data)
        for i in node.childlist:
            queue.append(i)

    for i in result:
        print(i)


def level_order_linebyline(root):
    if root == None:
        return

    queue = []
    result = []

    queue.append(root)

    while len(queue) > 0:
        count = len(queue)
        print("Q", result)
        result = []
        while count > 0:
            node = queue.pop(0)
            result.append(node.data)
            for i in node.childlist:
                queue.append(i)
        print(result)

    for i in result:
        print(i)


def Depth(node):
    if node is None:
        return 0

    else:
        maxdepth = 0
        for i in node.childlist:
            maxdepth = max(maxdepth, Depth(i))

        return maxdepth + 1


def printRoute(stack, root):
    if root == None:
        return

    # append this node to the path array
    stack.append(root.data)
    if len(root.childlist) == 0:
        print(" ".join([str(i) for i in stack]))

    # otherwise try both subtrees
    for i in root.childlist:
        printRoute(stack, i)
        stack.pop()


def findheight(parent, n):
    res = 0
    for i in range(n):
        p = i
        current = 1
        while parent[p] != -1:
            current = current + 1
            p = parent[p]
        res = max(current, res)
    return res
    # TIME COMPLEXITY = O(n) S(n)=O(1)


def isIsomorphic(n1, n2):

    # Both roots are None, trees isomorphic by definition
    if n1 is None and n2 is None:
        return True

    # Exactly one of the n1 and n2 is None, trees are not
    # isomorphic
    if n1 is None or n2 is None:
        return False

    if n1.data != n2.data:
        return False
    # There are two possible cases for n1 and n2 to be isomorphic
    # Case 1: The subtrees rooted at these nodes have NOT
    # been "Flipped".
    # Both of these subtrees have to be isomorphic, hence the &&
    # Case 2: The subtrees rooted at these nodes have
    # been "Flipped"
    return (isIsomorphic(n1.left, n2.left) and isIsomorphic(n1.right, n2.right)) or (
        isIsomorphic(n1.left, n2.right) and isIsomorphic(n1.right, n2.left)
    )
    # TIME COMPLEXITY = O(min(m,n)) where m and n are number of nodes in given trees.


def isQuasiIsomorphic(n1, n2):

    # Both roots are None, trees isomorphic by definition
    if n1 is None and n2 is None:
        return True

    # Exactly one of the n1 and n2 is None, trees are not
    # isomorphic
    if n1 is None or n2 is None:
        return False
    # There are two possible cases for n1 and n2 to be isomorphic
    # Case 1: The subtrees rooted at these nodes have NOT
    # been "Flipped".
    # Both of these subtrees have to be isomorphic, hence the &&
    # Case 2: The subtrees rooted at these nodes have
    # been "Flipped"
    return (isIsomorphic(n1.left, n2.left) and isIsomorphic(n1.right, n2.right)) or (
        isIsomorphic(n1.left, n2.right) and isIsomorphic(n1.right, n2.left)
    )


if __name__ == "__main__":
    root = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    f = Node(7)
    root.addchildren(a)
    root.addchildren(b)
    a.addchildren(c)
    b.addchildren(d)
    c.addchildren(e)
    e.addchildren(f)
    # printRoute([], root)
    level_order(root)
    # print(Depth(root))
    # parent = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
    # n = len(parent)
    # height = findheight(parent, n)
    # print("Height of the given tree is:", height)
    # # START-ISOMORPHIC
    # n1 = Node(1)
    # n1.left = Node(2)
    # n1.right = Node(3)
    # n1.left.left = Node(4)
    # n1.left.right = Node(5)
    # n1.right.left = Node(6)
    # n1.left.right.left = Node(7)
    # n1.left.right.right = Node(8)

    # n2 = Node(1)
    # n2.left = Node(3)
    # n2.right = Node(2)
    # n2.right.left = Node(4)
    # n2.right.right = Node(5)
    # n2.left.right = Node(6)
    # n2.right.right.left = Node(8)
    # n2.right.right.right = Node(7)
    # print("Yes") if (isIsomorphic(n1, n2) == True) else ("No")
    # # END

a=[1,2]
if a[-3]!=None:
    print(1)
else:
    print(0)