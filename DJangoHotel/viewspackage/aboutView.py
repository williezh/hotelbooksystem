# -*- coding: utf-8 -*-

from django.shortcuts import render
from qiniuyun.backend import QiniuPush
from qiniuyun.models import ImageAtQiniu
from .indexView import ImgList
from DJangoHotel.models import Hotel

def about(request):
    title='DJango Hotel'
    hotel=Hotel.objects.get(name='DJango Hotel')
    name=hotel.name
    description=hotel.description
    address=hotel.address

    imgObjs=ImageAtQiniu.objects.all()
    imgUrls=[QiniuPush.private_download_url(i.fullname) for i in imgObjs]
    imgs=ImgList()
    
    for i in imgUrls:        
        if 'hotel-logo' in i:
            imgs.logo=i

    return render(request,'about.html',{
        'title':title,
        'name':name,
        'description':description,
        'address':address,
        'img':imgs,
    })
