#!/usr/bin/env python

import mincemeat, sys, md5, md5, hashlib


inputstring = sys.argv[1]
print "Attacking " + str(inputstring) + " ..." +'\n'

def substrings(length, possibles):
  ret = []
  if length == 1:
    return list(possibles)
  else:
    subs = substrings(length -1, possibles)
    for chs in possibles:
      for sub in subs:
        ret.append(str(chs) + str(sub))
  return ret

alpha = "abcdefghijklmnopqrstuvwxyz0123456789"

allPos = []
for i in range(1, 5):
    allPos += substrings(i,alpha)

temp = []
temp.append(inputstring)
data =[]
counter = 1
for word in allPos:
  temp.append(word.rstrip())
  if counter % 4444 == 0:
    data.append(temp)
    temp = []
    temp.append(inputstring)	
  counter += 1
if temp != []:
   data.append(temp)

datasource = dict(enumerate(data))
#print datasource

def mapfn(k, v):
    import md5, hashlib
    for val in v:
	#print val 
	val=str(val)
    	#print (hashlib.md5(val).hexdigest()[:5])
        if (v[0]) == (hashlib.md5(str(val)).hexdigest()[:5]):
          print val
          yield v[0], val
  
def reducefn(k, vs):
    return list(set(vs))
    #remove redudant values 

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results


