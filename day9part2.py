#!/usr/bin/env python

import os
import string
import numpy as np
import copy
import queue

def check_first(nl,sp,width):
    if nl[0][0] < nl[0][1] and nl[0][0] < nl[1][0]:
        sp.append((0,0))

    for i in range(1,w):
        if nl[0][i] < nl[0][i-1] and nl[0][i] < nl[1][i] and nl[0][i] < nl[0][i+1]:
            sp.append((0,i))

    if nl[0][w] < nl[0][w-1] and nl[0][w] < nl[1][w]:
        sp.append((0,w))



def check_line(nl,sp,width,i):
    if nl[i][0] < nl[i][1] and nl[i][0] < nl[i+1][0] and nl[i][0] < nl[i-1][0]:
        sp.append((i,0))

    for j in range(1,w):
        if nl[i][j] < nl[i-1][j] and nl[i][j] < nl[i+1][j] and nl[i][j] < nl[i][j+1] and nl[i][j] < nl[i][j-1] :
            sp.append((i,j))

    if nl[i][w] < nl[i][w-1] and nl[i][w] < nl[i+1][w] and nl[i][w] < nl[i-1][w]:
        sp.append((i,w))


def check_last(nl,sp,width,height):
    if nl[h][0] < nl[h][1] and nl[h][0] < nl[h-1][0]:
        sp.append((h,0))

    for i in range(1,w):
        if nl[h][i] < nl[h][i-1] and nl[h][i] < nl[h-1][i] and nl[h][i] < nl[h][i+1]:
            sp.append((h,i))

    if nl[h][w] < nl[h][w-1] and nl[h][w] < nl[h-1][w]:
        sp.append((h,w))

def floodfill(nl,x,y):
    global area
    if nl[x][y] != 9:
        area += 1
        nl[x][y] = 9
        if x > 0:
            floodfill(nl,x-1,y)
        if x < len(nl[y]) - 1:
            floodfill(nl,x+1,y)
        if y > 0:
            floodfill(nl,x,y-1)
        if y < len(nl) - 1:
            floodfill(nl,x,y+1)

count = 0
width = 0
height = 0
tempfile = open("inputDay9.txt")
lines = tempfile.readlines()
num_list = []
for line in lines:
    numbers = line.strip()
    width = len(numbers) if width == 0 else width
    height += 1
    num_list.append(list(map(int,numbers)))

w = width - 1
h = height - 1
#Find all low_points
start_points = []
check_first(num_list,start_points,w)
for i in range(1,height-1):
    check_line(num_list,start_points,w,i)
check_last(num_list,start_points,w,h)

q = queue.PriorityQueue(maxsize=3)
for point in start_points:
    #flood fill
    area = 0
    floodfill(num_list,point[0],point[1])
    print(area)
    if q.qsize() < 3:
        q.put(area)
    else:
        first_val = q.get()
        if first_val > area:
            q.put(first_val)
        else:
            q.put(area)

count = q.get() * q.get() * q.get()

print(f"Answer: {count}")