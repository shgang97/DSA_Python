# "回文词"判定
from lineards.linear.deque import Deque


def palchecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addRear(ch)
    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
        lo = charDeque.removeRear()
        hi = charDeque.removeFront()
        if lo != hi:
            stillEqual = False
    return stillEqual


print(palchecker('上海自来水来自海上'))
print(palchecker('书临汉墨翰林书'))
