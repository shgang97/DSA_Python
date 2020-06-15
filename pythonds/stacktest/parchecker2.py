from pythonds.basic.stack import Stack


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    return balanced and s.isEmpty()


print(parChecker('{(((())[]))}'))
print(parChecker('[{()]}'))
