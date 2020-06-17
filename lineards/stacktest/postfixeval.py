from lineards.linear.stack import Stack
from lineards.stacktest.infixtopostfix import infixToPostfix


def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


postfixexpr=infixToPostfix('( 5 + 4 ) * 5 + 5')
print(postfixexpr)
print(postfixEval(postfixexpr))
