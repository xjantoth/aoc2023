#!/usr/bin/env python3
import re

data = open(0).readlines()
# data = open("input.txt").read()
instructions = data[0].strip("\n")
walking = {x[0]:(x[1], x[2]) for x in [re.findall(r"[A-Z]+", i) for i in data[1:] if i != "\n"]}
start = sorted(walking.items())[0][0]

len(instructions.split())

direction = {"R": 1, "L": 0}
s = 0
end = False
while True:
    if end:
        break
    for e, inst in enumerate(instructions):
        d = direction[inst]
        if walking[start][d] == "ZZZ":
            s += 1
            end = True
            print(f"found destionation after {s}, break!")
            break
        else:
            s += 1
            start = walking[start][d]
    instructions = instructions

print(s)

