#!/usr/local/bin/python
# -*- coding: utf-8 -*-
##
 #  @filename   :   main.cpp
 #  @brief      :   7.5inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 28 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import epd7in5
import Image
import ImageDraw
import ImageFont
import calendar
import time
import requests
import sys  
import urllib, json
import urllib2
import operator
import os 
import random
import threading



reload(sys)  
sys.setdefaultencoding('utf-8')
#import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384


todolist_items=0;


def main():


        displayTasks()
        wait=60;
        refresh_time=1000
        start_time=time.time()+refresh_time

        while True:
            print('restart  : current time ' + str(time.time()/60) + ' started time ' +str(start_time/60))
            if (time.time()-start_time)>0:
                start_time=time.time()+refresh_time # rest refresh time
                displayTasks()

            time.sleep(wait)
              
        

def restart_program():
    displayTasks()

def choose_random_loading_image():
    images=os.listdir("/home/pi/Eink-Pi/RaspberryPi/Eink/bmp/")
    loading_image=random.randint(0,len(images)-1)
    return images[loading_image]

def displayTasks():
    epd = epd7in5.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    image = Image.open('/home/pi/Eink-Pi/RaspberryPi/Eink/bmp/' + choose_random_loading_image())
    epd.display_frame(epd.get_frame_buffer(image))


    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)
if __name__ == '__main__':
    main()
