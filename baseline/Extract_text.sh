#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall
tool=$root/Update_NLU/FtrEtr.py

dataPath=$root/CESAR_data/annotated
objectfile=$dataPath/object-reference.xml

FtrPath=$root/Update_NLU/Feature/text
mkdir -p $FtrPath
ftrfile=$FtrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt
surfacefile=$FtrPath/word_Jun-Sun-3-09-09-17-2012.txt

for sub in $dataPath/*;
do
	name=$(basename $sub)
	objectfile=$sub/object-reference.xml
	ftrfile=$FtrPath/$name.txt
	surfacefile=$FtrPath/$name.word
	echo "$tool $objectfile $ftrfile $surfacefile"
	$tool $objectfile $ftrfile $surfacefile
done
