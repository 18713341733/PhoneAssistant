# -*- coding:utf-8 -*-
import re
str1 ="mCurrentFocus=Window{74cf3a u0 com.tencent.qqpimsecure/com.babytree.apps.pregnancy.activity.SailfishActivity}"

pattern = re.compile(r'u0\s*(.+?)\/')
res = re.findall(pattern, str1)
print ( res)