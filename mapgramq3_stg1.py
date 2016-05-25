#!/usr/bin/env python
import sys
import string
import re

totalwordlen = 0
allfield = {}
for line in sys.stdin:
  try:
    split_var=re.split(r'\t+', line)
    name = split_var[0]
    name = ''.join([i if ord(i) < 128 else ' ' for i in name])
    year = split_var[1]
    noofoccur = int(split_var[2])
# count no of char in a word
    line = name.strip()
    wordlen = 0
    for char in line:
      wordlen = wordlen + 1

    if year in allfield:
       allfield[year] = allfield[year][0]+wordlen*noofoccur,allfield[year][1]+noofoccur
    else:
       allfield[year] = wordlen*noofoccur,noofoccur
  except:		
    continue

for year in allfield:
  print '%s\t%s' % (year, allfield[year])
#print str(year)+'\t'+str(allfield[year])
