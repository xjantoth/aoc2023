#!/usr/bin/env python3
import re
from functools import reduce
data = open(0).readlines()
# data = open("input.txt").read()

regex = r"\d+"
inp1 = [i for i in zip(re.findall(regex, data[0]), re.findall(regex, data[1]))]

a = int(''.join(re.findall(regex, data[0])))
b = int(''.join(re.findall(regex, data[1])))

inp2 = [(a, b)]

def calculate(_input):
    res = []
    for e, i in enumerate(_input, start=1):
        c = 0 # initiate couner - how many times could you possibly go further than the best boat
        total_time, distance = i
        for _time in range(0, int(total_time)):
            # _time    = [0, 1, 2, ..., 7]
            # distance = 9
            # _time = 2
            if ((int(total_time) - _time) * _time) > int(distance):# (7 - 2) * 2 > 9
                c += 1
        res.append((e, c))
    return reduce((lambda x, y: x * y), [i[1] for i in res])

print(calculate(inp1), calculate(inp2))
