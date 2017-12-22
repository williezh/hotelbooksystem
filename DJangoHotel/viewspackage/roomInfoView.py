# -*- coding: utf-8 -*-

from django.shortcuts import render
from qiniuyun.backend import QiniuPush
from qiniuyun.models import ImageAtQiniu
from .indexView import ImgList
from DJangoHotel.models import RoomInfo

def roomInfo(request):
    rooms=RoomInfo.objects.all()
    imgObjs=ImageAtQiniu.objects.all()
    imgUrls=[QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs=ImgList()
    
    for i in imgUrls:        
        if 'hotel-logo' in i:
            imgs.logo=i
                
    return render(request,'roominfo.html',{'roomInfoList':rooms,'img':imgs})
