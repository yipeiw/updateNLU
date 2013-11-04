#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall
tool=$root/Update_NLU/eval.py

predictfile=$root/Update_NLU/baseline/Predict/Jun-Sun-3-09-09-17-2012_simple.txt

ftrPath=$root/Update_NLU/Feature/text
ftrfile=$ftrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt
surfacefile=$ftrPath/word_Jun-Sun-3-09-09-17-2012.txt

echo "$tool $predictfile $ftrfile $surfacefile"
$tool $predictfile $ftrfile $surfacefile

predictfile=$root/Update_NLU/baseline/Predict/Jun-Sun-3-09-09-17-2012_pure.txt
#echo "$tool $predictfile $ftrfile"
#$tool $predictfile $ftrfile

predictfile=$root/Update_NLU/baseline/Predict/Jun-Sun-3-09-09-17-2012_simulate.txt
#echo "$tool $predictfile $ftrfile"
#$tool $predictfile $ftrfile
