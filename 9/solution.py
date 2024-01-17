#!/usr/bin/env python3
import re
from itertools import pairwise

datar = [re.findall(r"\d+", i.strip("\n")) for i in open(0).readlines()]
data = [list(map(lambda x: int(x), i)) for i in datar]

# data = open("input.txt").read()

s1 = 0
for line in data:
    s = list()
    # print(line)
    s.append(line[-1])
    while any(line) is True:
        tmp = list()
        for a, b in pairwise(line):
            tmp.append(b-a)
        line = tmp
        s.append(tmp[-1])
        # print(tmp)
    print(s[::-1], sum(s[::-1]))
    s1 += sum(s[::-1])
print(s1)
    

