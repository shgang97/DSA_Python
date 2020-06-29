from treeds.tree.nodebinarytree import BinaryTree


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


if __name__ == '__main__':
    tree = BinaryTree('a')
    tree.insertLeft('b')
    tree.insertRight('c')
    tree.getRightChild().setRootVal('hello')
    tree.getRightChild().insertRight('d')
    print('********preorder************')
    preorder(tree)
    print('********postorder************')
    postorder(tree)
    print('********inorder************')
    inorder(tree)
