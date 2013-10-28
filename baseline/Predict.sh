#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall

tool=$root/Update_NLU/Predict.py

probfile=$root/Update_NLU/TrainData/TextOB/PredictTest_Jun-Sun-3-09-09-17-2012.txt

transitfile=$root/Update_NLU/baseline/model/transition/OBClass_Jun-Sun-3-09-09-17-2012.txt

ftrPath=$root/Update_NLU/Feature/text
ftrfile=$ftrPath/CESAR_Jun-Sun-3-09-09-17-2012.txt

predictPath=$root/Update_NLU/baseline/Predict
mkdir -p $predictPath

name=Jun-Sun-3-09-09-17-2012

$tool $probfile $transitfile $ftrfile $predictPath $name
