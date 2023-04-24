import pymysql
from xml.dom import minidom
import xml.dom.minidom

dom_tree = xml.dom.minidom.parse("..\default.xml")
root = dom_tree.documentElement
mysql_host = root.getElementsByTagName("element")[0].firstChild.nodeValue.strip("'")
mysql_user = root.getElementsByTagName("element")[1].firstChild.nodeValue.strip("'")
mysql_password = root.getElementsByTagName("element")[2].firstChild.nodeValue.strip("'")
mysql_db = root.getElementsByTagName("element")[3].firstChild.nodeValue.strip("'")

# 连接MySQL
conn = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    db=mysql_db,
    cursorclass=pymysql.cursors.DictCursor
)


def check_user(username, password):
    # 查询语句
    query = "SELECT * FROM users WHERE username=%s AND password=%s"

    # 执行查询
    with conn.cursor() as cursor:
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

    if result:
        # 用户存在
        return True
    else:
        # 用户不存在
        return False
