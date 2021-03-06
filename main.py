#!/usr/bin/env python
# -- coding:utf-8 --
# ------------------------ 
# @author: kyle-luo
# @file: main.py
# @time: 2020/7/7 14:27
# @desc:
# ------------------------
"""
@package:
    
"""

##########################
# - 树莓派小车识别项目
#   - 视觉
#       - 识别箭头颜色：
#           > 使用OpenCV的inRange()方法，提取出红色和绿色
#           > 使用该方法得到的就是二值图像
#       - 识别箭头方向
#           > 得到二值图像后，获得最小外接矩形的坐标
#           > 将矩形按照中线分开左半边和右半边
#           > 分别对两边做轮廓提取
#           > 计算两边得到轮廓的面积，哪边大就是指向哪一边的箭头
#   - 通信
##########################
import cv2
import numpy
import serial

import color
import direction
import mySer

if __name__ == '__main__':
    """
    1. 打开摄像头
    2. 识别颜色
    3. 判断方向
    4. 通信传输
    """

    # 打开摄像头
    capture = cv2.VideoCapture(0)

    # 串口通信
    # ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    try:
        results = []
        while True:

            ret, frame = capture.read()

            frame = cv2.imread("../img/GreenLeft.png")
            # rows, cols, channels = frame.shape
            # blank = numpy.ones([rows, cols, channels], frame.dtype)*255
            # frame = cv2.addWeighted(frame, 0.5, blank, 0.5, 3)
            # frame = numpy.uint8(numpy.clip((1.5*frame+10), 0, 255))
            # 识别颜色
            ret_, color_, image_, red, green = color.RecognizeColor(frame).recognizeColor()

            # 判断方向
            dirt_ = direction.JudgeDirection(image_).judgeDirection()

            # 与下位机通信
            result = mySer.AnalysisData(ret_, color_, dirt_).analysisData()

            results.append(result)

            # ser.write(result.encode())

            print(ret_.__str__() + " " + color_.__str__() + " " + dirt_.__str__() + " " + result)


            # cv2.imshow("frame", frame)
            # if image_.shape[0] != 0:
            #     dirt_ = direction.JudgeDirection(image_).judgeDirection()
            #     cv2.imshow("image", image_)
            #     print("方向是：" + dirt_.__str__())
            #
            # print("颜色是：" + color_.__str__())

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        # ser.close()
        pass

    cv2.destroyAllWindows()
