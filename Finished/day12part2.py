#!/usr/bin/env python
import os
import string
from collections import defaultdict

class Graph:
    def __init__(self,g):
        self.graph = g
        self.paths = 0
    def find_all_paths(self):
        visited = {}
        for key in self.graph.keys():
            visited[key] = False
        path = []

        self.find_all_paths_rec("start",visited,path,True)
        print(f"Answer: {self.paths}")
    
    def find_all_paths_rec(self,origin,visited,path,extra):
        if origin == "start" and len(path) > 1:
            return


        path.append(origin)
        if origin.islower():
            if path.count(origin) == 2 and extra == True:
                extra = False
            elif path.count(origin) < 2:
                pass
            else:
                path.pop()
                return

        if origin == "end":
            self.paths += 1
        else:
            for i in self.graph[origin]:
                self.find_all_paths_rec(i,visited,path,extra)
            

        visited[origin] = False
        path.pop()

        


temp_dict = defaultdict(list)

tempfile = open("inputDay12.txt")
lines = tempfile.readlines()
for line in lines:
    temp = line.strip().split('-')
    temp_dict[temp[0]].append(temp[1])
    temp_dict[temp[1]].append(temp[0])

graph = Graph(temp_dict)
graph.find_all_paths()
    
    



