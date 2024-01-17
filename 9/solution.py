#!/usr/bin/env python3
import re
from itertools import pairwise

datar = [re.findall(r"-?\d+", i.strip("\n")) for i in open(0).readlines()]
data = [list(map(lambda x: int(x), i)) for i in datar]

# data = open("input.txt").read()

s1, s2 = 0, 0
for line in data:
    end = list()
    start = list()
    # print(line)
    end.append(line[-1])
    start.append(line[0])
    while any(line) is True:
        tmp = list()
        for a, b in pairwise(line):
            tmp.append(b-a)
        line = tmp
        end.append(tmp[-1])
        start.append(tmp[0])
    print(end[::-1], sum(end[::-1]), start[::-1])
    s1 += sum(end[::-1])

    # part 2
    before = start[::-1]
    init = before[1] - before[0]

    for i in range(1, len(before)):
        if i + 1 == len(before):
            break
        else:
            init = before[i+1]- init
    s2 += init

print(s1, s2)
    

