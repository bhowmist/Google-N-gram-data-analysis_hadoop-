#!/usr/bin/env python
import sys
import string
import re

allfield = {}
for line in sys.stdin:
  try:
    (key,val) = line.split('\t',1)
#    print val
    newval = val.strip()
    newval = newval.replace('(','').replace(')','')
#    print newval
    newval1 = newval.split(',')
#    print newval1
    totalchar = int(newval1[0])
    totalnum = int(newval1[1])
    year = key
    if year in allfield:
       allfield[year] = allfield[year][0]+totalchar,allfield[year][1]+totalnum
    else:
       allfield[year] = totalchar,totalnum
  except:		
    continue

for year in allfield:
  print '%s\t%s' % (year, allfield[year])
	
