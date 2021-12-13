#!/usr/bin/env python

import os
import string

tempfile = open("inputDay10.txt")
lines = tempfile.readlines()

score_dict = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}

for line in lines:
    letter_queue = []
    line = line.rstrip('\n')
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
            print(f"Adding {letter} to score_dict")
            score_dict[letter] += 1
            break

score = 3 * score_dict[')'] + 57 * score_dict[']'] + 1197 * score_dict['}'] + 25137 * score_dict['>']

print(f"Answer: {score}")
        
