from treeds.tree.buildparsetree import buildParseTree


def printexp(tree):
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        sVal += printexp(tree.getRightChild()) + ')'
    return sVal


if __name__ == '__main__':
    tree = buildParseTree('( 3 + ( 4 * 8 ) )')
    print(printexp(tree))
