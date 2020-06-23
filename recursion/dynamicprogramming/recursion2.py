def recDC(coinValueList, change, knownResults):
    minConis = change
    if change in coinValueList:  # 递归基本结束条件
        knownResults[change] = 1  # 记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]  # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minConis:
                minConis = numCoins
                knownResults[change] = minConis
    return minConis


print(recDC([1, 5, 10, 25], 63, [0] * 64))
