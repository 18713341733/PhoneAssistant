# -*- coding:utf-8 -*-
#作者：陈帅
#实现功能：这个demo实现的btn开始与关闭的切换
import subprocess
'''
#开始抓取日志
def getLogcat(self, deviceID, deviceName):
    filename = self.log_path + "/" + deviceName + "_" + self.test_date + "_" + self.test_time + ".txt"
    logcat_file = open(filename, 'w')
    logcmd = "adb -s %s logcat -v time" % (deviceID)
    pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
    return pro, filename

#结束进程
def killPro(self, pro):
    pro.kill()
    #.close()是关闭文件的   .kill（）是杀掉进程a'''
class abc(object):

    def getLogcat1(self):
        filename ='a'+ ".txt"
        logcat_file = open(filename, 'w')
        logcmd = "adb logcat -v time"
        pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        return pro, filename
if __name__ == '__main__':
    abc().getLogcat1()

