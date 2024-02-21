#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#@author: aycabozyel
"""

#%%
#list

listInt = [0,1,2,3,4,5,7]
type(listInt)
listStr = ["mon","tue","wed","thu","fri","sat","sun"]
type(listStr)

val = listInt[2]
print(val)

val1 = listStr[-1]
print(val1)

dividedList = listInt[0:3]
print(dividedList )

listInt.append(6)
listInt.remove(7)
listStr.reverse()

print(listInt)
print(listStr)

unsortedlist = [2,3,5,1,6,8,9,7,0,4]
unsortedlist.sort()
print(unsortedlist)


listIntStr = [1,2,3,"monday"]



"""
append
clear
copy
count
extend
index
insert
pop
reverse
remove
sort
"""

#%%
#tuple

t = (1,2,3,4,5,6,7,3,3,3)

t.count(3)
t.index(5)



"""
count
index
"""

#%%
#dictionary


dictionary = {"mary":32,"jack":45,"john":13}

#mary, jack, john -> keys
# 32, 45,13 -> values

def getDictionary():
    dictionary = {"mary":32,"jack":45,"john":13}
    return dictionary

dic = getDictionary()
dic["mary"]
