#coding:utf-8
import os
import time
import pymysql
from kcsj.local_settings import DATABASES

dbconf=DATABASES.get('default')
config={'host':dbconf.get('HOST'),
    'user':dbconf.get('USER'),
    'passwd':dbconf.get('PASSWORD'),
    'port':dbconf.get('PORT'),
    'charset':'utf8',
    'db':dbconf.get('NAME'),
    }

insert_hotel="""insert into DJangoHotel_hotel(name,address,description)
                 values ('Django Hotel','GZ Tianhe Chebei',
                 'a warm hotel where you fell like at home')"""    
                 
insert_roominfo=[
    """insert into DJangoHotel_roominfo(name,price,total,description)
                 values ('标准间',158,10,
                 '简单、经济、干净、卫生')""",
    """insert into DJangoHotel_roominfo(name,price,total,description)
                 values ('豪华间',268,15,
                 '舒适、大气、富丽、瑭璜')""",
    """insert into DJangoHotel_roominfo(name,price,total,description)
                 values ('总统间',1888,2,
                 '霸气、开阔、尊贵、安全')""",
    ]                 
                

try:
    conn=pymysql.connect(**config)
    cur=conn.cursor()
    
    cur.execute(insert_hotel)
    for i in insert_roominfo:
        cur.execute(i)
        
    conn.commit()
    print('success to insert data')
    cur.close()
    conn.close()
except Exception as e:
    import traceback;traceback.print_exc()

    
