from Queue import Queue

import random

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm#打印速度
        self.currentTask=None#打印任务
        self.timeRemaining=0#任务倒计时
    #打印1秒
    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None
    #打印忙吗
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    #打印新作业
    def startNext(self,newTask):
        self.currentTask=newTask
        self.timeRemaining=newTask.getPages()\
            * 60 / self.pagerate

class Task:
    #生成时间
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    #等待时间
    def waitTime(self,currenttime):
        return currenttime-self.timestamp
#生成作业
def newPrintTask():
    num = random.randrange(1,181)
    if (num==180):
        return True
    else:
        return False