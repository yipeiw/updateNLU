#!/bin/bash

root=/home/yipeiw/Documents/Research-2013fall/Update_NLU

trainfile=$root/TrainData/TextOB/train10.txt
model=$root/baseline/model/simple_10t5
echo "maxent $trainfile -m $model"
maxent $trainfile -m $model

testfile=$root/TrainData/TextOB/test5.txt
output=$root/baseline/Predict/test5.result
echo "maxent -p -m $model -o output.txt $testfile"
maxent -p -m $model -o $output $testfile --detail
