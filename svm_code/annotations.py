#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu February  3 15:18:58 2016

@author: jaideep
"""

"""
generation of annotation for dataset
"""


import glob
import cv2
import os
import random
from PIL import Image


if __name__ == '__main__':
    images_1 = [cv2.imread(file) for file in glob.glob("/home/jaideep/Documents/personal/dataset/*.jpeg")]
    path = '/home/jaideep/Documents/personal/dataset/'
    # Store the image file names in a list as long as they are jpgs
    images_names = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.jpeg']
    sort_names = sorted(images_names)
    prev_num=0
    curr_num=0
    save_rand = random.uniform(0,1)
    for i in sort_names:
        curr_num = int(i[:i[:-5].find('_')])
        if(prev_num==0):
            prev_num=curr_num
        if(prev_num!=0 and curr_num!=prev_num):
            save_rand = random.uniform(0,1) 
            prev_num=curr_num
        with open("annotation.json","a") as test_file:
            test_file.write("%s: %3f\n"%(i,save_rand))