#!/usr/bin/env python3
import re

data = open(0).readlines()
instructions = data[0].strip("\n")
walking = {x[0]:(x[1], x[2]) for x in [re.findall(r"[A-Z]+", i) for i in data[1:] if i != "\n"]}
direction = {"R": 1, "L": 0}
start = "AAA"

s = 0
while start != "ZZZ":
    s += 1
    start = walking[start][direction[instructions[0]]]
    instructions = instructions[1:] + instructions[0]
    print(start)

print(s)

