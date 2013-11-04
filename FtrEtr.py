#!/usr/bin/env python

"""
feature extraction for maximum entropy classifier
label: object type
feature:bigram context and speaker (left and right);
	part-of-speech (l1,l2,c,r1,r2) 
info: word boundary
pre-label
"""

import sys
sys.path.append('/home/yipeiw/Documents/Research-2013fall/Tool/AnnotationAnalysis')
from read_write_annotation_files import *

from collections import defaultdict
import re
from nltk.tag import pos_tag  
from nltk.tokenize import word_tokenize 
import pronoun

pronounfile = '/home/yipeiw/Documents/Research-2013fall/coreference-baseline/English_Pronoun.list'
pronoun_list = pronoun.LoadPronoun(pronounfile)
print pronoun_list

objectfile=sys.argv[1]
ftrfile=sys.argv[2]
surfacefile = sys.argv[3]


def Denoise(word):
        if word.find('%')!=-1 or word.find('<')!=-1 or word.find('>')!=-1:
                return ""
        return re.sub('\^|_|@','', word).strip()

def GetPOS(left, right, words):
	left_list = []
	right_list = []
	for word in left:
		if word!="NA":
			left_list.append(word)
	for word in right:
		if word != "NA":
			right_list.append(word)

	left_text = " ".join(left_list)
	right_text = " ".join(right_list)

	pair_list = pos_tag(word_tokenize(left_text+" "+words+" "+right_text))
	left_pos = [pair_list[i][1] for i in range(0, len(left))]
	right_pos = [pair_list[i][1] for i in range(len(pair_list)-len(right), len(pair_list))]
	return left_pos+right_pos

def GetTokens(bound, win, word_map, word_num, increase):
	tok_list = []
	spk_list = []
	start = bound
	while len(tok_list) < win:
		if start >= word_num or start < 0:
			for i in range(0, win-len(tok_list)):
				tok_list.append("NA")
				spk_list.append("NA")
			break
				
		filter_word = Denoise(word_map[start][0])
		if filter_word!="":
			tokens = word_tokenize(filter_word)
			tok_list += tokens
			spk_list.append(word_map[start][1])

		if increase:
			start += 1
		else:
			start = start - 1
	
	if not increase:
		tok_list.reverse()
		spk_list.reverse()

	return tok_list, spk_list

def GetText(idlist, word_map):
	text_list =[word_map[idx][0] for idx in sorted(idlist)]
	return " ".join(text_list)
	
def GetContext(words, window, word_map, word_num):
	idlist = [int(word.name.split('_')[1]) for word in words]
	(left, right) = (min(idlist), max(idlist))
	part_sent = []
	tok_left, spk_left = GetTokens(left-1, window, word_map, word_num, False)
	tok_right, spk_right = GetTokens(right+1, window, word_map, word_num, True)
	pos_list = GetPOS(tok_left, tok_right, GetText(idlist, word_map))
	return tok_left+tok_right, pos_list, spk_left+spk_right

def outputIns(fout, context, pos_list, spk_list, label, words, pre, spk, pronoun_tag):
	ftr = " ".join(context+pos_list+spk_list)
	idlist = [int(word.name.split('_')[1]) for word in words]
	(l, r) = (min(idlist), max(idlist))
	fout.write("%s %s %s-%s %s %s %s\n" % (spk, pronoun_tag, l, r, pre, label, ftr))	

def cleanLB(lb):
	end = lb.find('(')
	word_list = lb[0:end].strip().split()
	return "_".join(word_list)

def GetTag(words, ob, pronoun_list, track_dict):
	judge = pronoun.IsPronoun(words, pronoun_list, 'dict')
	if judge == 2:
		if track_dict[ob]:
			return "coref-pronoun"
		else:
			return "single-pronoun"
	if judge==1:
			return "1-pronoun"
	if judge == 0:
		return "non-pronoun"

fout = open(ftrfile, 'w')
f = open(surfacefile, 'w')

window = 2
words, annotations, notes = read_annotation_file(objectfile)

word_map = {int(word.name.split('_')[1]): (word.text, word.speaker) for word in words}
word_num = len(word_map.keys())

track_dict = defaultdict(bool)
pre="NONE"
for ai in annotations:
	label = cleanLB(ai.label)
	idlist=[int(word.name.split('_')[1]) for word in ai.words]
	word_text = GetText(idlist, word_map)

	pronoun_tag = GetTag(word_text, ai.object_parameter, pronoun_list, track_dict)

	context, pos_list, spk_list = GetContext(ai.words, window, word_map, word_num)
	outputIns(fout, context, pos_list, spk_list, label, ai.words, pre, ai.words[0].speaker, pronoun_tag)
	f.write("%s\n" % (word_text))
	pre = label
	track_dict[ai.object_parameter] = True

fout.close()
f.close()

