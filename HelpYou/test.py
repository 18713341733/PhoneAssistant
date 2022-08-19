# -*- coding:utf-8 -*-
#作者：张兴，陈帅
#修改日期：2018.7.7
#修改功能：链接手机时，增加了对是否安装adb的判断
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from MainPage import *
import os
import re
import subprocess
out = subprocess.getstatusoutput('adb devices -l')
print(out)
out1 = subprocess.getstatusoutput('adb devices')