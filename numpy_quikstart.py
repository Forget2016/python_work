import numpy as np

#the array of the numpy , there are three types of copy
#method
a = np.arange(12)

"""this is different name for the same ndarray objects
if change the copy , the origin array will change too"""

b = a
b.shape = (3, 4)

"""the second way is view or shallow copy, the copy change
the number, the origin number will change ,but the shape
do not affect"""
c = a.view()
c.flags #which check the information of c like owndata,wwriteable

c.shape = (2,6) #just change the shape of c, the a don't change
c[0,3] = 1232 #change the a`s number

"""
deep copy does create a complete copy of the array and its data
"""
d = a.copy()
d[0,0] = 244 # change the d and don't change the a