#!/usr/bin/env python
import mincemeat,sys

fi=open(sys.argv[1],'r')
data=list(fi)
fi.close()
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
        yield 'Sum', int(v)
	yield 'Count', 1
	yield 'std', int(v)

def reducefn(k, vs):
  if k=="Sum" or k=="Count":
    result = sum(vs)
    return result
  else:
    count=len(vs)
    mean=sum(vs)/count
    var=0
    for i in vs:
       var=var+((i-mean)**2)
    std=(var/count)**0.5       
    return std

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print "Count:",results["Count"]
print "Sum:",results["Sum"]
print "Standard_deviation:",results["std"]


