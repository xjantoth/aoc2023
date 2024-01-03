#!/usr/bin/env python3
import re
from termcolor import colored
import time

data = open(0).read().splitlines()

ci = [e for e, _ in enumerate(data)]     # valid column indexes
ri = [e for e, _ in enumerate(data[0])]  # valid row indexes

t = []
for e, i in enumerate(data):
    left = data[e-1] if e -1 in ci else f"."*len(data[0])
    middle = data[e]
    right = data[e+1] if e + 1 in ci else f"."*len(data[0])
    t.append((left, middle, {s.group(): s.span() for s in re.finditer(r"\d+", middle)},right))

s1 = 0

unmatched = []
for e, c in enumerate(t):
    for num, s in c[2].items():
        u = list(map(lambda x: t[e][0][x], range(*(s[0]-1 if s[0]-1 in ri else s[0], s[1]+1 if s[1]+1 in ri else s[1])))) # left site or row above
        b = list(map(lambda x: t[e][3][x], range(*(s[0]-1 if s[0]-1 in ri else s[0], s[1]+1 if s[1]+1 in ri else s[1])))) # rigth site or row below
        ub = f"{num}{''.join(u+b).replace('.', '')}"# returns number or numbers that has special character on right or left

        # Detecting whether or not particular number has special 
        # character on left or right without any spaces e.g   ...$100...200*..
        sites = re.findall(r"(?=(\d+[#/@&=\*+%\-\$]|[#/@&=\*+%\-\$]\d+))", c[1])
        pretty = list(map(lambda x: re.sub(r'[#/@&=\*+%\-\$]', '',x), sites))

        if len(pretty) > 0 and num in pretty:
            print("--pretty condition>: ", colored(num, "green"), sites)
            s1 += int(num)
            print(c[0])
            print(re.sub(str(num), colored(num, 'green'), c[1]))
            print(c[3])
            print("row", e)
        elif bool(re.search(r'[#/@&=\*+%\-\$]', ub)):
            print("--bool condition-->: ", colored(num,"green"), ub)
            s1 += int(num)
            print(c[0])
            print(re.sub(str(num), colored(num, 'green'), c[1]))
            print(c[3])
            print("row", e)
        else:
            unmatched.append(num)
    print("H-"*30, "\n")

        # time.sleep(1)
        # print("\n"*5)
            
print("s1: ",s1)

print(sum(list(map(int, unmatched))))
print(unmatched)

# for i in t:
#     print(i)
