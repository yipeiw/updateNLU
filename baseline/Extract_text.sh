#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall
tool=$root/Update_NLU/FtrEtr.py

dataPath=$root/CESAR_data/annotated/CESAR_Jun-Sun-3-09-09-17-2012
objectfile=$dataPath/object-reference.xml

FtrPath=$root/Update_NLU/Feature/text
mkdir -p $FtrPath
ftrfile=$FtrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt

$tool $objectfile $ftrfile
