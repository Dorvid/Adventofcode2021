#!/usr/bin/env python

import os
import string
import queue

tempfile = open("inputDay10.txt")
lines = tempfile.readlines()

scores = []
value_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
for line in lines:
    letter_queue = []
    line = line.rstrip('\n')
    is_corrupted = False
    for letter in line:
        #If opening bracket, etc.
        if letter == '(':
            letter_queue.append(')')
            continue
        if letter == '[':
            letter_queue.append(']')
            continue
        if letter == '{':
            letter_queue.append('}')
            continue
        if letter == '<':
            letter_queue.append('>')
            continue
        #Else if closing
        exepecting = letter_queue[len(letter_queue)-1]
        letter_queue.pop()
        if letter != exepecting:
            is_corrupted = True
    if is_corrupted:
        continue
    #Auto complete part
    curr_score = 0
    for expected in reversed(letter_queue):
        curr_score *= 5
        letter = letter_queue.pop()
        curr_score += value_dict[letter]
    scores.append(curr_score)
scores.sort()
middle = int((len(scores)/2))
print(f"Answer: {scores[middle]}")
    