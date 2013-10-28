#!/usr/bin/env python

import sys
from collections import defaultdict

predictfile = sys.argv[1]
ftrfile = sys.argv[2]

def LoadInfo(ftrfile):
        info_list = []
        for line in open(ftrfile):
                linelist = line.strip().split()
                spk, pronoun_tag, bound, pretag, tag = linelist[0:5]
                info_list += [(tag, pretag, bound, spk, pronoun_tag)]
        return info_list

def LoadPredict(predictfile):
	result_list = []
	for line in open(predictfile):
		linelist = line.strip().split()
		(idx, trueLB, LB) = linelist[0:3]
		result_list += [(trueLB, trueLB==LB)]
	return result_list

def measure(result_list):
	correct_num = 0
	total = len(result_list)
	accuracy_dict = defaultdict(int)
	class_num = defaultdict(int)

	for i in range(0, total):
		truth, correct = result_list[i]
		if correct:
			correct_num += 1
			accuracy_dict[truth] += 1
		class_num[truth] += 1

	accuracy_list = []
	for name in class_num.keys():
		accuracy_list += [(name, float(accuracy_dict[name])/class_num[name])]

	return float(correct_num)/total, accuracy_list

def TypeAnalysis(pronounTags, info_list, result_list):
	accuracy_dict = defaultdict(int)
	class_num = defaultdict(int)
	for i in range(0, len(info_list)):
		truth, correct = result_list[i]
		pronoun_tag = info_list[i][4]
                if correct:
                        accuracy_dict[pronoun_tag] += 1
                class_num[pronoun_tag] += 1	
	accuracy_list = []
        for name in class_num.keys():
                accuracy_list += [(name, float(accuracy_dict[name])/class_num[name])]

        return accuracy_list


result_list = LoadPredict(predictfile)
info_list = LoadInfo(ftrfile)
print result_list[0:5]
accuracy, class_list = measure(result_list)
print "Accuracy:", accuracy
for name, val in class_list:
	print name, val

pronounTags=["coref-pronoun", "single-pronoun", "1-pronoun", "non-pronoun"]
print "\ntype analysis:"
type_performance = TypeAnalysis(pronounTags, info_list, result_list)
for name, val in type_performance:
	print name, val

