#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:55:18 2016

@author: jaideep
"""

import glob
import cv2
import os
import random
import numpy as np
from PIL import Image


if __name__ == '__main__':
    read_images = [cv2.imread(file) for file in glob.glob("/home/jaideep/Documents/personal/dataset/*.jpeg")]
    img = []
    addj_size = (500,500)
    count=1
    for i in read_images:
        aspect_ratio = i.shape[0]/i.shape[1]
        i_resized = cv2.resize(i,dsize=(500,500),interpolation=cv2.INTER_CUBIC)
        #im = Image.fromarray(i_resized)
        #im.save(str(count) + '.jpeg')
        count = count+1
        img.append(cv2.cvtColor(i_resized,cv2.COLOR_BGR2GRAY))
        