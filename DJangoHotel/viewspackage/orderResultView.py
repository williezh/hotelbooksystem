# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from qiniuyun.backend import QiniuPush
from qiniuyun.models import ImageAtQiniu
from indexView import ImgList
from DJangoHotel.models import Order,RoomInfo,Customer
import time
import datetime
from random import randint

def orderResult(request):
    imgObjs=ImageAtQiniu.objects.all()
    imgUrls=[QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs=ImgList()
    
    for i in imgUrls:        
        if 'hotel-logo' in i:
            imgs.logo=i
                
    tel,name,IDcard= request.GET['tel'],request.GET['name'],request.GET['IDcard']
    if Customer.objects.all():
        cc=Customer.objects.filter(IDcard=IDcard)
    else:
        cc=[]
    for c in cc:
        if c and c.tel==tel and c.name==name:
            tempCustomer=c
            break
    else:
        tempCustomer=Customer(tel=tel,name=name,IDcard=IDcard)        
        tempCustomer.save()

    tempOrder=Order()
    tempOrder.customer = tempCustomer
    tempOrder.roomtype = request.GET['roomtype']
    
    
    begin,end = request.GET['begin'],request.GET['end']     
    tempOrder.begin = (datetime.datetime.strptime(begin , '%Y-%m-%d')).date()
    tempOrder.end = (datetime.datetime.strptime(end , '%Y-%m-%d')).date()
    period = (tempOrder.end - tempOrder.begin).days 
    if period==0:period=1        
        
    price = 0

    if tempOrder.roomtype == 'standard':
        price = (RoomInfo.objects.get(name='标准间')).price

    elif tempOrder.roomtype =='better':
        price = (RoomInfo.objects.get(name='豪华间')).price

    elif tempOrder.roomtype =='president':
        price = (RoomInfo.objects.get(name='总统间')).price

    tempOrder.roomnum=randint(1,10)
    tempOrder.totalprice = period * price
    tempOrder.save()


    return render(request,'orderresult.html',{'order':tempOrder,'img':imgs})
