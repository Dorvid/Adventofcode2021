#!/usr/bin/env python

import os
import string
import numpy as np
import copy

class bingo_board:
    board = []
    state = []
    won = False

    def __init__(self):
        self.state = [[False,False,False,False,False]
            ,[False,False,False,False,False]
            ,[False,False,False,False,False]
            ,[False,False,False,False,False]
            ,[False,False,False,False,False]]
        self.won = False
    def fill_board(self,arr):
        self.board = arr.copy()

    def find_number(self,num: int):
        for i in range(5):
            for j in range(5):
                number = self.board[i][j]
                if number == num:
                    self.state[i][j] = True
                    return

    def validate_board(self):
        cnt_v = 0
        cnt_h = 0
        for i in range(5):
            for j in range(5):
                if self.state[i][j] == True:
                    cnt_h += 1
                if self.state[j][i] == True:
                    cnt_v += 1
            if cnt_v == 5 or cnt_h == 5:
                #Bingo!
                return True
            cnt_v = 0
            cnt_h = 0
        return False        
    
    def unmarked_sum(self):
        output = 0
        for i in range(5):
            for j in range(5):
                if self.state[i][j] == False:
                    output += self.board[i][j]
        
        return output


tempfile = open("inputDay4.txt")
first_line = tempfile.readline()
temp_num_list = first_line.split(',')
numbers = list(map(int,temp_num_list))
bingo_boards = []

empty_arr = [[]]*5
input = tempfile.readlines()
temp_arr = []

for i in range(int((len(input)/6))):    
    temp_arr = []
    for j in range(1,6):
        temp_line = input[j+i*6].split()
        temp_ints = list(map(int,temp_line))
        temp_arr.append(temp_ints)
    
    if temp_arr != empty_arr:
        new_board = bingo_board()
        new_board.fill_board(copy.deepcopy(temp_arr))
        bingo_boards.append(new_board)

found = False
wins_left = len(bingo_boards)
for i in numbers:
    for j in bingo_boards:
        if j.won == False:
            j.find_number(i)
            if j.validate_board():
                j.won = True
                wins_left -= 1
                if wins_left == 0:
                    answer = j.unmarked_sum() * i
                    print("Answer: " + str(answer))
                    found = True
                    break
    if found:
        break
    

