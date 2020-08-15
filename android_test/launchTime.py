import os
import time
import csv

class App(object):
    def __init__(self):
        self.content=''
        self.startTime=''
    def launchApp(self):
        cmd='adb shell am start  -W -n com.dayu.haibao/com.dayu.haibao.ui.activity.StartAnimActivity'
        self.content=os.popen(cmd).read().split('\n')
        print(self.content)
        # c=self.content
        # self.content=self.content.read()
        # print(self.content)
        # print(c1)
    def stopApp(self):
        cmd='adb shell input keyevent 3'
        os.popen(cmd)
    def getLaunchTime(self):
       for line in self.content:
           if 'ThisTime'in line:
               self.startTime=line.split(':')[1].strip()
               d=self.startTime
               # print(self.startTime)
               print(d)
               break
       return self.startTime



class Controller(object):
    def __init__(self,count):
        self.app=App()
        self.counter=count
        # self.alldata=[('timestamp','elapsedtime')]
        self.alldata=[]
    def test_process(self):
        self.app.launchApp()
        elpasedtime=self.app.getLaunchTime()
        time.sleep(3)
        self.app.stopApp()
        time.sleep(3)

        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,elpasedtime))


    def run(self):
        while self.counter>0:
            self.test_process()
            self.counter-=1
    def getCurrentTime(self):
        currentTime=time.ctime()
        return currentTime

    def collectAllData(self):
        pass
    def saveDataToCSV(self):
        # csvfile=file('test.csv','wb')
        # writer=csv.writer(csvfile)
        # writer.writerrows(self.alldata)
        # csvfile.close()


        with open('test.csv','w',newline='') as f:
            csvwriter=csv.writer(f,dialect='excel')

            csvwriter.writerow(self.alldata)

        # pass
if __name__ == '__main__':
    controller=Controller(3)
    controller.run()
    controller.saveDataToCSV()