#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall

tool=$root/Update_NLU/trainfile.py

ftrPath=$root/Update_NLU/Feature/text
ftrfile=$ftrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt

trainPath=$root/Update_NLU/TrainData/TextOB
mkdir -p $trainPath
trainfile=$trainPath/CESAR_Jun-Sun-3-09-09-17-2012.txt

$tool $ftrfile $trainfile
