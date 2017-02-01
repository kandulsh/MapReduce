#!/usr/bin/env python
import mincemeat

data=[2]
for i in range(3,100001,2):
  # if (j%5 == 0 and len(str(j))!=1):
   #      continue
   data.append(i)

# The data source can be any dictionary-like object 
datasource = dict(enumerate(data))

def mapfn(k, v): 
     a=str(v)
     b=a[::-1]
     if a==b:
       yield 'Number',v

def reducefn(k, vs):
     a=[]
     for j in vs: 
       if all(j%i!=0 for i in range(2,int(j**0.5)+1)):
         a.append(j)	     
     return a

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "Total number of primes which are palindromes in given range:", len(results["Number"])


