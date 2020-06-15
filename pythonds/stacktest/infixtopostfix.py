from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    # 构造一个字典记录操作符优先级
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    # 定义一个栈保存操作符
    opStack = Stack()
    # 定义一个列表报错后缀表达式
    postfixList = []
    # 解析表达式到单词列表
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)


if __name__ == '__main__':
    postfixExpr = infixToPostfix(' ( 5 + 4 ) * 5 + 5 ')
    print(postfixExpr)
