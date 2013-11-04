#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall

tool=$root/Update_NLU/Predict.py

probfile=$root/Update_NLU/baseline/Predict/test5.result

transitfile=$root/Update_NLU/baseline/model/transition/OBClass_Jun-Sun-3-09-09-17-2012.txt

ftrPath=$root/Update_NLU/Feature/text
ftrfile=$ftrPath/test5.txt

predictPath=$root/Update_NLU/baseline/Predict
mkdir -p $predictPath

name=train10test5

$tool $probfile $transitfile $ftrfile $predictPath $name
