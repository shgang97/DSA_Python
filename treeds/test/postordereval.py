import operator

from treeds.tree.buildparsetree import buildParseTree


def postordereval(tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


if __name__ == '__main__':
    tree = buildParseTree('( 3 + ( 4 * 8 ) )')
    print(postordereval(tree))
