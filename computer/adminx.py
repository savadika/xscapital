# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         adminx.py
# Description:
# Author:       ylf
# Date:         2019-05-16
# -------------------------------------------------------------------------------
import xadmin
from .models import Computer


class ComputerAdmin(object):
    list_display = [
        'type',
        'sn',
        'owner',
        'buy_date',
        'keep_years',
        'has_expired',
        'manager']
    search_fields=[
        'type',
        'sn',
        'owner',
        'buy_date',
        'keep_years',
        'has_expired',
        'manager'
    ]


xadmin.site.register(Computer, ComputerAdmin)
