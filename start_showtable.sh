#!/bin/bash

#real_path
real_path=`cd $(dirname $0) && pwd`
cd ${real_path}

cat ${real_path}/per_file.txt|while read per
do
    /usr/bin/python ${real_path}/P_table.py ${per} > ${real_path}/${per%%_*}_permission.txt
done
