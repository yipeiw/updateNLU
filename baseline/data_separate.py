#!/usr/bin/env python

import os.path as path

dataPath='/home/yipeiw/Documents/Research-2013fall/Update_NLU/Feature/text'
trainfile='/home/yipeiw/Documents/Research-2013fall/CESAR_data/train.list'
testfile='/home/yipeiw/Documents/Research-2013fall/CESAR_data/test.list'

trainlist = [line.strip() for line in open(trainfile)]
testlist = [line.strip() for line in open(testfile)]

TrainPath = '/home/yipeiw/Documents/Research-2013fall/Update_NLU/TrainData/TextOB'
outputTrain = path.join(TrainPath, "train10.txt")
outputTest = path.join(TrainPath, "test5.txt")

infoTrain = path.join(dataPath, 'train10.txt')
infoTest = path.join(dataPath, 'test5.txt')

TrainWord = path.join(TrainPath, "train10.word")
TestWord = path.join(TrainPath, "test5.word")

f1 = open(outputTrain, 'w')
f1w = open(TrainWord, 'w')
f1t = open(infoTrain, 'w')

f2 = open(outputTest, 'w')
f2w = open(TestWord, 'w')
f2t = open(infoTest, 'w')

for name in trainlist:
	trainfile = path.join(dataPath, name + '.txt')
	for line in open(trainfile):
		f1t.write(line)
		linelist = line.strip().split()
        	item_list = [linelist[i] for i in range(3, len(linelist))]
        	f1.write(" ".join(item_list)+'\n')
	trainword = path.join(dataPath, name + '.word')
	for line in open(trainword):
        	f1w.write(line)
f1.close()
f1w.close()
f1t.close()

for name in testlist:
	testfile = path.join(dataPath, name + '.txt')
        for line in open(testfile):
		f2t.write(line)
		linelist = line.strip().split()
                item_list = [linelist[i] for i in range(3, len(linelist))]
                f2.write(" ".join(item_list)+'\n')

	testword = path.join(dataPath, name + '.word')
        for line in open(testword):
                f2w.write(line)
f2.close()
f2w.close()
f2t.close()
