#!/usr/bin/env python

import sys
from collections import defaultdict

ftrfile = sys.argv[1]
output = sys.argv[2]

transit = defaultdict(int)
prob = defaultdict(int)

for line in open(ftrfile):
	linelist = line.strip().split()
	pre = linelist[2]
	current = linelist[3]
	transit[(pre, current)] += 1
	prob[pre] += 1

fout = open(output, 'w')
for pre, current in transit.keys():
	val = transit[(pre, current)]
	fout.write("%s|%s %.6f\n" % (current, pre, float(val)/prob[pre]))
fout.close()
