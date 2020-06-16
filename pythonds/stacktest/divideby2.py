from pythonds.linear.stack import Stack


def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber  //= 2
    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString


print(divideBy2(43))
