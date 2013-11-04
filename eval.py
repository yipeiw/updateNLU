#!/usr/bin/env python

import sys
from collections import defaultdict
import re

predictfile = sys.argv[1]
ftrfile = sys.argv[2]

surface_list = []
if len(sys.argv) >= 3:
	surfacefile = sys.argv[3]
	surface_list = [line.strip() for line in open(surfacefile)]

def Denoise(word):
        if word.find('%')!=-1 or word.find('<')!=-1 or word.find('>')!=-1:
                return ""
        return re.sub('\^|_|@','', word).strip()

def LoadInfo(ftrfile):
        info_list = []
        for line in open(ftrfile):
                linelist = line.strip().split()
                spk, pronoun_tag, bound, pretag, tag = linelist[0:5]
                info_list += [(tag, pretag, bound, spk, pronoun_tag)]
        return info_list

def LoadPredict(predictfile):
	result_list = []
	top2_list = []
	top3_list = []
	for line in open(predictfile):
		linelist = line.strip().split()
		(idx, trueLB, LB) = linelist[0:3]
		result_list += [(trueLB, trueLB==LB)]

		LB2 = linelist[4].split(':')[0]
		top2_list += [(trueLB, (trueLB==LB or trueLB==LB2))]

		LB3 = linelist[5].split(':')[0]
		top3_list += [(trueLB, (trueLB==LB or trueLB==LB2 or trueLB==LB3))]
	return result_list, top2_list, top3_list

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
		if info_list[i][0]=='Other':
			continue

		truth, correct = result_list[i]
		pronoun_tag = info_list[i][4]
                if correct:
                        accuracy_dict[pronoun_tag] += 1
                class_num[pronoun_tag] += 1	
	accuracy_list = []
        for name in class_num.keys():
                accuracy_list += [(name, float(accuracy_dict[name])/class_num[name])]

        return accuracy_list

def TypeMarix(pronounTags, info_list, result_list):
        accuracy_dict = defaultdict(int)
        class_num = defaultdict(int)
        for i in range(0, len(info_list)):
		if info_list[i][0]=='Other':
                        continue

                truth, correct = result_list[i]
                pronoun_tag = info_list[i][4]
                if correct:
                        accuracy_dict[pronoun_tag, truth] += 1
                class_num[pronoun_tag, truth] += 1
	print "type analysis matrix"
        for ptag, name in class_num.keys():
                print ptag, name, float(accuracy_dict[ptag, name])/class_num[ptag, name]

def InfoAnalysis(surface_list, info_list):
	Pro_surface_dict = defaultdict(int)
	Ob_surface_dict = defaultdict(int)
	for i in range(0, len(info_list)):
		tag, pretag, bound, spk, pronoun_tag = info_list[i]	
		word = Denoise(surface_list[i])
		if pronoun_tag != "non-pronoun" and tag != "Other":
			Pro_surface_dict[(pronoun_tag, word)] += 1
		Ob_surface_dict[(tag, word)] += 1
	
	f = open("surface_analysis.log", 'w')
	total = sum([num for num in Pro_surface_dict.values()])
	
	pro_list = defaultdict(list)
	for pro, word in Pro_surface_dict.keys():
		pro_list[pro] += [(word, Pro_surface_dict[(pro, word)])]
	for pro, infolist in pro_list.items():
		f.write("\n%s\n" % (pro))
		for word, num in sorted(infolist, key=lambda item:item[1], reverse=True):
			f.write("%s %s\n" % (word, num))

	Ob_list = defaultdict(list)
	for Ob, word in Ob_surface_dict.keys():
		Ob_list[Ob] += [(word, Ob_surface_dict[(Ob, word)])]
	for ob, infolist in Ob_list.items():
                f.write("\n%s\n" % (ob))
                for word, num in sorted(infolist, key=lambda item:item[1], reverse=True):
                        f.write("%s %s\n" % (word, num))
	f.close()

result_list, top2_list, top3_list = LoadPredict(predictfile)
info_list = LoadInfo(ftrfile)
accuracy, class_list = measure(result_list)
print "Accuracy:", accuracy
for name, val in class_list:
	print name, val

accuracy2, class_list2 = measure(top2_list)
print "\nTop2 Accuracy:", accuracy2
for name, val in class_list2:
        print name, val

accuracy3, class_list3 = measure(top3_list)
print "\nTop3 Accuracy:", accuracy3
for name, val in class_list3:
        print name, val

pronounTags=["coref-pronoun", "single-pronoun", "1-pronoun", "non-pronoun"]
print "\ntype analysis:"
type_performance = TypeAnalysis(pronounTags, info_list, result_list)
for name, val in type_performance:
	print name, val

print ""
TypeMarix(pronounTags, info_list, result_list)

InfoAnalysis(surface_list, info_list)
