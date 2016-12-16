
from  collections import OrderedDict #only import the OrderedDict Fn
import globalval as gv
from globalfunc import *  # import all functions

# test email function

def testmymail():
    a=gv.a  # value from globalval
	# code from previous examples
    ae=list(a.items())
    af=OrderedDict(sorted(ae,key=lambda  t:t[1][0]+t[1][1] ))
    ag=str(list ((k,v)for k,v in af.items()))

    sendmymail(ag, "sorted list")


if __name__ == "__main__":
    testmymail()
