#!/usr/bin/env python
# -- coding:utf-8 --
# ------------------------ 
# @author: kyle-luo
# @file: direction
# @time: 2020/7/7 19:34
# @desc: 判断箭头方向
# ------------------------
"""
@package:
    
"""
import cv2

from utils import DIRECTION


class JudgeDirection:
    """判断图片中的箭头指向的方向

    Args:
        image:(numpy) 待判断的图片

    Returns:
        dirt:(DIRECTION) 判断的方向，左边或者右边

    """

    def __init__(self, image):
        self.image = image

    @staticmethod
    def __getBoxArea(img):
        _, _, w, h = cv2.boundingRect(img)
        return w * h

    def judgeDirection(self):
        """
        判断图片中箭头的方向

        > 按照中线将图片分成两张图片，左边一张，右边一张
        > 分别对两张图片做外接矩形
        > 判断两个图片的外接矩形的面积，那边大，箭头就是指向哪边
        """

        width = self.image.shape[1]
        mid = width//2

        tmp_img = self.image.copy()

        img_left = tmp_img[:, 0: mid]
        img_right = tmp_img[:, mid: width]

        left_area = self.__getBoxArea(img_left)
        right_area = self.__getBoxArea(img_right)

        return DIRECTION.LEFT if (left_area > right_area) else DIRECTION.RIGHT
