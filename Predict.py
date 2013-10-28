#!/usr/bin/env python

import sys
from collections import defaultdict
import os.path as path

probfile = sys.argv[1]
transitfile = sys.argv[2]
ftrfile = sys.argv[3]
predictPath = sys.argv[4]
name = sys.argv[5]

def LoadProb(probfile):
	data_list = []
	for line in open(probfile):
		linelist = line.strip().split()
		prob_list = []
		for i in range(0, len(linelist), 2):
			name = linelist[i]
			prob = float(linelist[i+1])
			prob_list += [(name, prob)]
		data_list += [prob_list]
	return data_list

def LoadInfo(ftrfile):
	info_list = []
	for line in open(ftrfile):
		linelist = line.strip().split()
		spk, bound, pretag, tag = linelist[0:4]
		info_list += [(tag, pretag, bound, spk)]
	return info_list

def LoadTransit(transitfile):
	transit = defaultdict(float)
	for line in open(transitfile):
		relation, val = line.strip().split()
		(cur, pre) = relation.split('|')
		transit[(cur, pre)] = float(val)
	return transit

def SelectBest(distribution):
	rank = sorted(distribution, key=lambda item:item[1], reverse=True)
	return rank[0][0]

def update_predict(class_num, prob_list, info_list, transition):
	first = True
	simple_list = []
	pure_list = []
	simulate_list = []
	uniform = float(1)/class_num

	for i in range(0, len(prob_list)):
		distribution = prob_list[i]
		pure=[]
		simple=[]
		simulate=[]
		if first:
			for name, prob in distribution:
	                        pure += [(name, prob*uniform)]
        	                simple += [(name, prob)]
                	        simulate += [(name, prob*uniform)]
			first = False
		else:
			for name, prob in distribution:
				pure += [(name, prob*transition[(name, last_predict)])]
				simple += [(name, prob)]
				simulate += [(name, prob*transition[(name, last_tag)])]
		pure_list += [(SelectBest(pure), pure)]
		simple_list += [(SelectBest(simple), simple)]
		simulate_list += [(SelectBest(simulate), simulate)]
		last_predict = SelectBest(pure)
		last_tag = info_list[i][0]

	return simple_list, pure_list, simulate_list

def outputPredict(info_list, predict_list, outputfile):
	fout = open(outputfile, 'w')
	for i in range(0, len(info_list)):
		info = "%s %s " % (i, info_list[i][0])
        	(tag, item) = predict_list[i]
		outputline = tag
		total = sum([val for name, val in item])
        	for name, val in item:
                	outputline += " %s:%s" % (name, val/total)
        	fout.write(info + outputline+'\n')
	fout.close()


prob_list = LoadProb(probfile)
info_list = LoadInfo(ftrfile)
transition = LoadTransit(transitfile)
class_num = int(len(prob_list[0])/2)

simple_list, pure_list, simulate_list = update_predict(class_num, prob_list, info_list, transition)

output_simple = path.join(predictPath, name+'_simple.txt')
outputPredict(info_list, simple_list, output_simple)

output_pure = path.join(predictPath, name+'_pure.txt')
outputPredict(info_list, pure_list, output_pure)

output_simulate = path.join(predictPath, name + '_simulate.txt')
outputPredict(info_list, simulate_list, output_simulate)
