#!/usr/bin/env python3
import re
from itertools import chain
data = open(0).read()
# data = open("input.txt").read()

regex = r"(.\n?)*(?=\n\n|\Z)"
matches = re.finditer(regex, data, re.MULTILINE)
t = [i.group() for i in matches if i.group() != '']
p = t[1:] # first element are seeds themselves
seeds = list(map(int, re.findall(r"\d+", t[0])))
seeds2 = list(map(int, re.findall(r"\d+", t[0])))

s = {re.sub(r"\smap:", "", i.split("\n")[0]): 
     [list(map(int, x)) for x in [re.findall(r"\d+", x) for x in i.split("\n")[1:] if len(re.findall(r"\d+", x))]] 
     for i in p}
# "s" returns a structure likefollowing:
# {
#     'seed-to-soil map:': [[50, 98, 2], [52, 50, 48]], 
#     'soil-to-fertilizer map:': [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 


# seeds = [i for i in range(79, 79+14)] + [i for i in range(55, 55+13)]
x = [tuple(seeds2[i:i + 2]) for i in range(0, len(seeds2), 2)]

print(x)
    


step = "seed"
while True:
    key = [w for w in s.keys() if w.split("-")[0] == step]
    if len(key) == 0:
        break

    key = key[0] # take first element since there will always be just one key
    for seed in seeds:
        idx_seed = seeds.index(seed)
        for p in s[key]: # p: [d, s , r]
            if seed in range(p[1], p[1]+p[2]):
                seeds[idx_seed] = p[0] + abs(seed - p[1])

    step = key.split("-")[2]

print("solution1:", min(seeds))

