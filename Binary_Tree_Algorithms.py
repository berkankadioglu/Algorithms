
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal_recursive(root):

    out = [root.val]

    if root.left:
        out += (preorder_traversal_recursive(root.left))
    if root.right:
        out += (preorder_traversal_recursive(root.right))

    return out


def preorder_traversal_iterative(root):
    pass


def inorder_traversal_recursive(root):

    out = []

    if root:
        out += inorder_traversal_recursive(root.left)
        out.append(root.val)
        out += inorder_traversal_recursive(root.right)

    return out


def inorder_traversal_iterative(root):
    pass


def postorder_traversal_recursive(root):

    out = []

    if root:
        out += postorder_traversal_recursive(root.left)
        out += postorder_traversal_recursive(root.right)
        out.append(root.val)

    return out


def postorder_traversal_iterative(root):
    pass


if __name__ == '__main__':
    # Example tree can be visualized at leetcode:
    # https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/

    n1 = TreeNode('F')
    n2 = TreeNode('B')
    n3 = TreeNode('A')
    n4 = TreeNode('D')
    n5 = TreeNode('C')
    n6 = TreeNode('E')
    n7 = TreeNode('G')
    n8 = TreeNode('I')
    n9 = TreeNode('H')

    n1.left = n2
    n1.right = n7

    n2.left = n3
    n2.right = n4

    n4.left = n5
    n4.right = n6

    n7.right = n8

    n8.left = n9

    print(preorder_traversal_recursive(root=n1))
    print(inorder_traversal_recursive(root=n1))
    print(postorder_traversal_recursive(root=n1))
