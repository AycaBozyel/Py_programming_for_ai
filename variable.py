#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#@author: aycabozyel
"""

#%%
#variable
var1 = 10
var2 = 15

day = "monday"

var3 = 10.0

#%%
#string
s = "Today is monday"

variable_type = type(s)

print(s)

var4 = "ankara"
var5 = "izmir"
var6 = var4 + var5

print(var6)

lenght = len(var6)
print(lenght)

print(var6[7])

#%%
#number

integer_num = -50
float_num = 30.7

#%%
#built in functions
str1 = "test"

float(integer_num)
int(float_num)
round(float_num)

str2 = "1003"
int(str2)

print(str2*3)

#%%
#user defined functions

var7 = 10
var8 = 34

def myCalculator(varx,vary):
    output = (((varx+vary)*40)/200.9)*varx/vary
    print(output)

myCalculator(var7,var8)

#%%
#default and flexible functions

def calculate_circle_circumference(r, pi = 3.14):
    result = 2*pi*r
    return result

print(calculate_circle_circumference(2))

def calculate_bmi(weight,height, *args):
    print(args)
    output = weight/(height*height)
    return output


calculate_bmi(82, 1.62, 30, 27, 90)
