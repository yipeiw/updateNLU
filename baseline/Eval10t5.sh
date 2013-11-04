#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall
tool=$root/Update_NLU/eval.py

predictfile=$root/Update_NLU/baseline/Predict/train10test5_simple.txt

ftrPath=$root/Update_NLU/Feature/text
ftrfile=$ftrPath/test5.word
surfacefile=$root/Update_NLU/TrainData/TextOB/test5.word

echo "$tool $predictfile $ftrfile $surfacefile"
$tool $predictfile $ftrfile $surfacefile
