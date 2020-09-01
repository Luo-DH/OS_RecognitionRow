#!/usr/bin/env python
# -- coding:utf-8 --
# ------------------------ 
# @author: kyle-luo
# @file: template
# @time: 2020/7/12 10:21
# @desc: 使用模板匹配方法，检测箭头的方向
# ------------------------
"""
@package:
    
"""

##########################
# - 将输入的图像转换成灰度图
# - 使用模板匹配方法找到图像中指向左边或者右边的箭头
##########################
import cv2

if __name__ == '__main__':

    left_template = cv2.imread("../img/GreenLeft.png", 0)
    left_template = cv2.resize(left_template, (100, 100))
    right_template = cv2.imread("../img/RedRight.png", 0)

    img = cv2.imread("../img/GreenLeft2.png", cv2.IMREAD_GRAYSCALE)


    cv2.imshow("left", left_template)
    cv2.imshow("right", right_template)
    cv2.imshow("image", img)
    cv2.waitKey(0)
