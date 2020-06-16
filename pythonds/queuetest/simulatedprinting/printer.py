# 定义一份打印机类
class Printer:
    # 初始化打印机属性
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 打印倒计时

    # 打印1秒
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 判断当前是否有打印任务
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    # 打印新任务
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate
