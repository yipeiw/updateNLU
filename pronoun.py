#!/usr/bin/env python

from collections import defaultdict
from nltk import word_tokenize

def LoadPronoun(pronounfile):
	pronoun_dict = defaultdict(int)
	for line in open(pronounfile):
		linelist = line.strip().split(",")
		if linelist[len(linelist)-1].find("PT")!=-1:
			person = int(linelist[len(linelist)-1].split(":")[1])
			if person==1 or person==2:
				pronoun_dict[linelist[0]] = 1
				continue
		pronoun_dict[linelist[0]] = 2
	return pronoun_dict

def IsPronoun(words, pronoun_list, kind):
	for token in word_tokenize(words):
		if pronoun_list[token]>0:
			return pronoun_list[token]
	return 0
