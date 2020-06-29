import operator

from treeds.tree.buildparsetree import buildParseTree


def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


if __name__ == '__main__':
    parsetree = buildParseTree('( 3 + ( 4 * 8 ) )')
    print(parsetree)
    res = evaluate(parsetree)
    print(res)
