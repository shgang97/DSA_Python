from pythonds.linear.stack import Stack


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base
    newstring = ''
    while not remstack.isEmpty():
        newstring += digits[remstack.pop()]
    return newstring


print(baseConverter(25, 2))
print(baseConverter(25, 16))
