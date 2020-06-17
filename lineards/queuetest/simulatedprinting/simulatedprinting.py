from lineards.linear.queue import Queue
from lineards.queuetest.simulatedprinting.printer import Printer
from lineards.queuetest.simulatedprinting.task import Task, newPrintTask


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)
        labprinter.tick()
    averageWait = sum(waitingTimes) / len(waitingTimes)
    print('Average Wait %6.2f secs %3d tasks remaining.' % (averageWait, printQueue.size()))


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 10)
