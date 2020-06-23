def recMC(coinValueList, change):
    minConis = change
    if change in coinValueList:
        return 1  # 最小规模，直接返回
    else:
        for i in [c for c in coinValueList if c <= change]:
            # 调用自身，减小规模：每次减去一种硬币面值，挑选最小数量
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minConis:
                minConis = numCoins
    return minConis


print(recMC([1, 5, 10, 25], 63))
