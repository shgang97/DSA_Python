def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change + 1):
        # 1.初始化一个最大值
        coinCount = cents
        newCoin = 1  # 初始化新加硬币
        # 2.减去每个硬币，向后查最小硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 3.得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin


if __name__ == '__main__':
    amnt = 75
    clist = [1, 5, 10, 21, 25]
    coinUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    print("Making change for", amnt, 'requires')
    print(dpMakeChange(clist, amnt, coinCount, coinUsed), 'coins')
    print('They are:')
    print('The used list is as follows:')
    print(coinUsed)
