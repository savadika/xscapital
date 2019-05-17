# -*— coding:utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.
class Computer(models.Model):
    type=models.CharField(max_length=20,verbose_name=u"型号")
    sn=models.CharField(max_length=30,verbose_name='SN编号')
    owner=models.CharField(max_length=20,verbose_name=u'所有者')
    buy_date=models.DateField(verbose_name=u"购买日期")
    keep_years=models.IntegerField(default=5,verbose_name=u'保修年限')
    has_expired=models.BooleanField(default=False,verbose_name='是否过保')
    manager=models.CharField(max_length=20,verbose_name='管理员')
    add_time=models.CharField(max_length=30,default=datetime.now,verbose_name='记录时间')

    class Meta:
        verbose_name=u'电脑信息表'
        verbose_name_plural=verbose_name