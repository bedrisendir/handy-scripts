#!/bin/bash +vx

for machines in `cat $1`

do

ssh $machines "$2"

done
