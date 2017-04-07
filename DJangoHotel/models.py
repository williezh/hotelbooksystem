# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

ROOM_TPYE_CHOICES=(
    ('standard','标准间'),
    ('better','豪华间'),
    ('president','总统间')
)

ORDER_STATE_CHOICES=(
    ('will','预定中'),
    ('run','执行中'),
    ('end','已结束'),
    ('destroyed','已废弃'),
)


class Hotel(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    address = models.CharField(max_length=50)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name  

class Customer(models.Model):
#    id = models.AutoField(primary_key=True, default='SOME STRING')
    tel = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='someone')
    IDcard=models.CharField(max_length=30,null=True,blank=True)
    
    def __unicode__(self):
        return self.name    

class RoomInfo(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    price = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Order(models.Model):    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    roomtype = models.CharField(max_length=45,choices= ROOM_TPYE_CHOICES)
    begin = models.DateField()
    end = models.DateField()
    totalprice = models.IntegerField()
    state=models.CharField(max_length=45,choices=ORDER_STATE_CHOICES)

    def __unicode__(self):
        return self.id



