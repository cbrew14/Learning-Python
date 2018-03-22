import statistics as s
"""or do something like this
from statistics import variance as v, mean as m
or
from statistics import *
using this method, no letter is nescessary before the command"""
example_list = [2, 3, 7, 8, 9, 5, 6, 8]
x = s.mean(example_list)
y = s.stdev(example_list)
z = s.median(example_list)
xx = s.mode(example_list)
xy = s.variance(example_list)
print(x, y, z, xx, xy)
