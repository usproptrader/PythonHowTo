
from  collections import defaultdict,OrderedDict

a=defaultdict(list)
# we use {} for defaultdict
# contents are a keys plus value (tuple)
a={'abcd':(12,34),'defc':(22,56),'gggg':(11,12),'hhhh':(11,33)}
# a new dict
ac={'dd':(23,44)}
# aupdate dict{a} with dict {ac]
a.update(ac)
# add 56 to 11
ad=a['defc'][1]+a['gggg'][0]
# the itesm,keys and values as lists
ae=list(a.items())
aee=list(a.keys())
aef=list(a.values())
# sort the items by value1 +value2 46,78,33,44
af=OrderedDict(sorted(ae,key=lambda  t:t[1][0]+t[1][1] ))
# create a sorted list
ag=list ((k,v)for k,v in af.items())

ah=[]
aj=()
ak=""
# more manipulation
# get each item key,value
for k,v in ae:
# get the 2 values of the tuple
    u,x=v
# add value1 to value2
    y=v[0]+v[1]
# ad to a list a tuple
    ah +=[(k,y,u,x)]
# add to a list
    aj +=(k,y)
# add the string of the tuple with no ()
    ak +=str("".join(","+str(v).strip("()")))
# add all the keys to a string
am=""
for k in a:
    am+=k
b=''