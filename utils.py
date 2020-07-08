#!/usr/bin/env python
# -- coding:utf-8 --
# ------------------------ 
# @author: kyle-luo
# @file: utils.py
# @time: 2020/7/7 15:11
# @desc: 工具类，定义常量
# ------------------------
"""
@package:
    
"""

from enum import Enum


class COLOR(Enum):

    RED = 0

    GREEN = 1

    OTHER = 3


class COLOR_BOUNDARY(Enum):
    RED_LOWER_BOUNDARY = (0, 0, 150)
    RED_UPPER_BOUNDARY = (100, 100, 255)

    GREEN_LOWER_BOUNDARY = (0, 150, 0)
    GREEN_UPPER_BOUNDARY = (100, 255, 100)


class DIRECTION(Enum):

    LEFT = 0
    RIGHT = 1
