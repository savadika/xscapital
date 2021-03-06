# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-05-16 02:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='型号')),
                ('sn', models.CharField(max_length=30, verbose_name='SN编号')),
                ('owner', models.CharField(max_length=20, verbose_name='所有者')),
                ('buy_date', models.DateField(verbose_name='购买日期')),
                ('keep_years', models.IntegerField(default=5, verbose_name='保修年限')),
                ('has_expired', models.BooleanField(default=False, verbose_name='是否过保')),
                ('manager', models.CharField(max_length=20, verbose_name='管理员')),
                ('add_time', models.CharField(default=datetime.datetime.now, max_length=30, verbose_name='记录时间')),
            ],
            options={
                'verbose_name': '电脑信息表',
                'verbose_name_plural': '电脑信息表',
            },
        ),
    ]
