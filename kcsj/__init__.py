#coding=utf-8

import os
if 'SERVER_SOFTWARE' not in os.environ:
    import pymysql
    pymysql.install_as_MySQLdb()


#设置编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
