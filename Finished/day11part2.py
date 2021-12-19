#!/usr/bin/env python

import os

def print_list(nl):
    for i in range(10):
        print(f"{nl[i][0]}{nl[i][1]}{nl[i][2]}{nl[i][3]}{nl[i][4]}{nl[i][5]}{nl[i][6]}{nl[i][7]}{nl[i][8]}{nl[i][9]}")
    print('\n')

def inc_adjecent(nl,f,x,y):
    if f[x][y] == False:
        f[x][y] = True
        if x > 0:
            nl[x-1][y] += 1
            if y > 0:
                nl[x-1][y-1] += 1
            if y < 9:
                nl[x-1][y+1] += 1
        if x < 9:
            nl[x+1][y] += 1
            if y > 0:
                nl[x+1][y-1] += 1
            if y < 9:
                nl[x+1][y+1] += 1
        if y > 0:
            nl[x][y-1] += 1
        if y < 9:
            nl[x][y+1] += 1
        return True
    return False

tempfile = open("inputDay11.txt")
lines = tempfile.readlines()
num_list = []
for line in lines:
    numbers = line.strip()
    num_list.append(list(map(int,numbers)))



print_list(num_list)
step = 1
while(True):
    flashed = [[False for x in range(10)]for y in range(10)]
    flashes = 0
    #Increment all values
    for i in range(10):
        for j in range(10):
            num_list[i][j] += 1

    while(True):
        count = 0
        for i in range(10):
            for j in range(10):
                if num_list[i][j] >= 10:
                    if inc_adjecent(num_list,flashed,i,j):
                        count += 1
        if count == 0:
            break


    for i in range(10):
        for j in range(10):
            if num_list[i][j] > 9:
                flashes += 1
                num_list[i][j] = 0
    
    if flashes == 100:
        print(f"Answer: {step}")
        break
    step += 1



