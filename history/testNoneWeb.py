# -*- coding: UTF-8 -*-
import os
import re
port = 5000

ret = os.popen("netstat -nao|findstr " + str(port))
str_list = ret.read().encode().decode('gbk')
print(str_list)
ret_list = re.split('',str_list)
print(ret_list)
try:
    process_pid = list(ret_list[0].split())[-1]
    os.popen('taskkill /pid ' + str(process_pid) + ' /F')
    print ("端口已被释放")
except:
    print ("端口未被使用")

