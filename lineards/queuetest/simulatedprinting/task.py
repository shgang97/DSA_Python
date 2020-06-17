import random


# 定义一份任务类
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


# 定义一个以每秒1/180的概率生成新任务的方法
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
