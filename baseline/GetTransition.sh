#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall
tool=$root/Update_NLU/estimate_transit.py

FtrPath=$root/Update_NLU/Feature/text
ftrfile=$FtrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt

outputPath=$root/Update_NLU/baseline/model/transition
mkdir -p $outputPath
outputfile=$outputPath/OBClass_Jun-Sun-3-09-09-17-2012.txt

$tool $ftrfile $outputfile
