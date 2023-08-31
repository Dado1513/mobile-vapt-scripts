#!/usr/bin/bash
mkdir $1
packagename=$2
cd $1

for apkpath in $(adb shell pm path $packagename); do  awk -F"package:" ' {system("adb pull " $2)}' <<< $apkpath  ; done