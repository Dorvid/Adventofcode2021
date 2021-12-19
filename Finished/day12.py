#!/usr/bin/env python
import os
import string
from collections import defaultdict

class Graph:
    def __init__(self,g,v):
        self.graph = g
        self.V = v
        self.paths = 0
    def find_all_paths(self):
        visited = {}
        for key in self.graph.keys():
            visited[key] = False
        path = []
        print(visited)

        self.find_all_paths_rec("start",visited,path)
        print(f"Answer: {self.paths}")
    
    def find_all_paths_rec(self,origin,visited,path):
        if origin.islower():
            visited[origin] = True

        path.append(origin)
        if origin == "end":
            print(path)
            self.paths += 1
        else:
            for i in self.graph[origin]:
                if visited[i] == False:
                    self.find_all_paths_rec(i,visited,path)
            

        path.pop()
        visited[origin] = False
        


temp_dict = defaultdict(list)

tempfile = open("inputDay12.txt")
lines = tempfile.readlines()
for line in lines:
    temp = line.strip().split('-')
    temp_dict[temp[0]].append(temp[1])
    temp_dict[temp[1]].append(temp[0])

graph = Graph(temp_dict,len(temp_dict))
graph.find_all_paths()
    
    



