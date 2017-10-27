#!/bin/sh

#cat <&0\ | grep -P "n-é-verbo.*\t" 
#~ cat <&0 | grep -P "[\t].*\bvir\b.*\bvir\b.*"
#~ cat <&0 | grep -P "#.*\t"
#cat <&0 | grep -P "\?.*\t"
#cat <&0 | grep -P "\?.*\t"
# trocar palavra por lema
cat <&0 | cut -f 2

