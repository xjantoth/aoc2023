#!/usr/bin/env python3
import re
from math import lcm

data = open(0).readlines()
# data = open("input.txt").read()
instructions = data[0].strip("\n")
walking = {x[0]:(x[1], x[2]) for x in [re.findall(r"\w+", i.strip("\n")) for i in data[1:] if i != "\n"]}
start = [i for i in list(map(lambda x: x if x[-1] == "A" else None, walking.keys())) if i]
print("...", start)
direction = {"R": 1, "L": 0}

# start is a list
counts = list()
for i in start: # list of all keys ending with "A"
    c = i
    s = 0
    while i.endswith("Z") is False:
        s += 1
        i = walking[i][direction[instructions[0]]]
        instructions = instructions[1:] + instructions[0]
    counts.append((c, i, s))

l = lcm(*list(map(lambda x: x[2], counts)))
print(l)

