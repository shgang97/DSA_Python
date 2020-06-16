from pythonds.linear.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.size())
    return simqueue.dequeue()


print(hotPotato(['Bill', 'Bavid', 'Susan', 'jane', 'Kent', 'Brad'], 7))
