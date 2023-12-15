#!/usr/bin/env python3
import re
import math

m = {"red": 12, "green": 13, "blue": 14}

data = open(0).read().splitlines()
rg = re.compile(f"\w+")
rn = re.compile(f"\d+")

s1 = s2 = 0
for i in data:
    # [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
    t = i.split(":")[1].split(";")
    dicts = [dict(map(lambda ii,jj : (ii,jj) , rg.findall(di)[1::2], rg.findall(di)[::2])) for di in t]
    
    if all([all((m.get(k) >= int(v) for k, v in item.items())) for item in dicts]):
        s1 += int(rn.search(i.split(":")[0]).group())
    # example of tpls:
    # [('red', '1'), ('green', '2'), ('green', '2'), ('blue', '3'), ('red', '4'), ('blue', '6')]
    tpls = [(k, v) for i in dicts for k,v in i.items()]

    # Part 2
    f = {"red": 0, "green": 0, "blue": 0}
    # trying to find the highes number of each color from tpls andrewriting it every time the program 
    # finds higher number 
    # [('red', '1'), ('green', '2'), ('green', '2'), ('blue', '3'), ('red', '4'), ('blue', '6')]
    h = [f.update({kk[0]: int(kk[1])}) for kk in tpls if int(kk[1]) > f[kk[0]] ]
    s2 += math.prod(f.values())

print(s1, s2)


    
