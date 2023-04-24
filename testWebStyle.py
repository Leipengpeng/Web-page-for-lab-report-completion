# 打开XML文件
from xml.dom import minidom

import xml.dom.minidom

# 打开XML文件
dom_tree = xml.dom.minidom.parse("default.xml")

# 获取根元素
root = dom_tree.documentElement

# 获取'mysql_password'元素
mysql_password_elem = root.getElementsByTagName("element")[2]

# 获取'mysql_password'元素的文本内容
mysql_password = mysql_password_elem.firstChild.nodeValue.strip("'")

# 打印'mysql_password'元素的值
print(mysql_password)
