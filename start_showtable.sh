#!/bin/bash
cat per_file.txt|while read per
do
    #echo "/tmp/${per%%_*}_permission.txt"
    /usr/bin/python P_table.py ${per} > /tmp/${per%%_*}_permission.txt
done
