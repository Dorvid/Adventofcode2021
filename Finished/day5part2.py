#!/usr/bin/env python

import os
import string
import numpy as np
import copy
import time
from graphics import *

def get_angle(val1,val2):
    if val1 == val2:
        return 0
    elif val1 < val2:
        return 1
    else:
        return -1
 

win = GraphWin(width = 800, height = 800)
win.setCoords(-100,-100,1100,1100)
myRect = Rectangle(Point(0,0),Point(1000,1000))
myRect.draw(win)

line_map = [[0 for x in range(1000)]for y in range(1000)]

tempfile = open("inputDay5.txt")
input = tempfile.readlines()
for line in input:
    temp_str = line.replace(" -> ",',')
    temp_vals = temp_str.split(',')
    vals = list(map(int,temp_vals))
    
    x = vals[0]
    y = vals[1]

    x_inc = get_angle(vals[0],vals[2])
    y_inc = get_angle(vals[1],vals[3])

    #Draw line in window
    win_line = Line(Point(vals[0],vals[1]),Point(vals[2],vals[3]))
    win_line.draw(win)

    #Fill map
    while(True):
        line_map[x][y] += 1
        if x == vals[2] and y == vals[3]:
            break
        x += x_inc #if (x != vals[2]) else 0
        y += y_inc #if (y != vals[3]) else 0


cnt = 0
for i in range(1000):
    for j in range(1000):
        if line_map[i][j] >= 2:
            cnt += 1

           

print("Answer: " + str(cnt))


time.sleep(10)