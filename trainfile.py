#!/usr/bin/env python

import sys

ftrfile = sys.argv[1]
trainfile = sys.argv[2]

f = open(trainfile, 'w')
for line in open(ftrfile):
	linelist = line.strip().split()
	item_list = [linelist[i] for i in range(3, len(linelist))]
	f.write(" ".join(item_list)+'\n')
		
f.close()

