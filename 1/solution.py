#!/usr/bin/env python3
import re

m = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

data = [line for line in open(0).read().splitlines()]

processed = []
for i in data:
    regex = re.compile(r'(?=(\d|%s))' % '|'.join(map(re.escape, m)))
    t = regex.findall(i)
    f = "".join(list(map(lambda x: m.get(x, x), t)))
    processed.append(f)

def compute(data: list[str]) -> int:
    """Consumes list of strings"""
    s = 0
    for i in data:
        n = "".join(re.findall(r'\d+', i))
        if len(n) > 0:
            s += int(f"{n[0]}{n[-1]}")
    return s

print("solutions: ", compute(data), compute(processed))

def hello(a):
    return true
