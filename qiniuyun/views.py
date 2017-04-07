#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import ImageAtQiniu
from qiniuyun.backend import QiniuPush as QP

class UploadForm(forms.Form):
    name = forms.CharField(required=False)
    img = forms.FileField()

def upload(request):
    if request.method == 'POST':
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            uname = uf.cleaned_data['name']
            hImg = uf.cleaned_data['img']  
            if not uname.strip():         
                uname=hImg.name            
            u = ImageAtQiniu()
            u.fullname = QP.put_data(uname,hImg)                       
            u.save()
            request.session['img_fullname'] = u.fullname
            return HttpResponseRedirect('/upload/done/')
    else:
        uf = UploadForm()
        uf.img=QP.private_download_url(QP.get_url('default.jpg'))
    return render(request, 'qiniuyun/upload.html', {'uf': uf})

def upload_result(request):
    name=request.session['img_fullname']
    img_url=QP.private_download_url(name)
    return render(request, 'qiniuyun/upload_result.html', {
        'img_fullname': name,
        'img_url':img_url,
        })

class Img(object):
    def __init__(self,name,url):
        self.name=name
        self.url=url
        
def show_imgs(request):
    imgs=ImageAtQiniu.objects.all()
    L=[Img(i.fullname,QP.private_download_url(i.fullname)) for i in imgs]
    return render(request, 'qiniuyun/show_imgs.html', {'imgList':L,})   
        
         
