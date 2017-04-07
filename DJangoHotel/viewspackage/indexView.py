# -*- coding: utf-8 -*-
from django.shortcuts import render
from qiniuyun.backend import QiniuPush

from DJangoHotel.models import Hotel
from qiniuyun.models import ImageAtQiniu

class ImgList(object):
    def __init__(self,logo=None,k1=None,k2=None,k3=None):
        self.logo=logo
        self.key_home_1=k1
        self.key_home_2=k2
        self.key_home_3=k3
        
def index(request):
    hotel=Hotel.objects.get(name='DJango Hotel')
    description=hotel.description
    
    imgObjs=ImageAtQiniu.objects.all()
    imgUrls=[QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs=ImgList()
    
    for i in imgUrls:        
        if 'hotel-logo' in i:
            imgs.logo=i            
        elif 'key_home_1' in i:
            imgs.key_home_1=i
        elif 'key_home_2' in i:
            imgs.key_home_2=i
        elif 'key_home_3' in i:
            imgs.key_home_3=i

    return render(request,'index.html',{'description':description,'img':imgs})


 
