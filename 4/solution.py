#!/usr/bin/env python3
import re

data = open(0).read().splitlines()
s1 = 0
s2 = {i: 0 for i in range(1, len(data)+1)}

for i in data:
    t = re.findall(r"\d+|\|", i)
    winer = t[1:t.index("|")]
    guess = t[t.index("|")+1:]
    print(set(winer).intersection(guess))
    c = len(set(winer).intersection(guess))
    print(c)
    if c > 0:
        if c > 1:
            s1+=1*(2**(c-1))
        else:
            s1 += 1

print(s1) # 28276 too high
print(s2)




