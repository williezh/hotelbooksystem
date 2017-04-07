#coding:utf-8
import pymysql

from importlib import import_module
#search the dirname of local_settings.py and import it
with open('manage.py') as f:
    s=f.read()
d=re.search(r'DJANGO_SETTINGS_MODULE.*?,\s*"(.+?)settings',s).group(1)
mo=import_module(d+'local_settings')

dbconf=mo.DATABASES.get('default')
config={'host':dbconf.get('HOST'),
    'user':dbconf.get('USER'),
    'passwd':dbconf.get('PASSWORD'),
    'port':dbconf.get('PORT'),
    'charset':'utf8',
    }
database=dbconf.get('NAME')

try:
    conn=pymysql.connect(**config)
    cur=conn.cursor()
    
    cur.execute('create database if not exists {}'.format(database))
    #conn.select_db(database)
    conn.commit()    

    cur.close()
    conn.close()
except Exception,e:
     print "SQL Error: %s" % (e)

    
