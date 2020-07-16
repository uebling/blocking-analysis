#!/usr/bin/python
'''

blocking.py [options] file1 file2 ... fileN

Text here.'''

from math import sqrt
import argparse
import re
#import os
#import sys

filename = "FCIMCStats"

column = 5

delimiters = ["\t"," ",","]

f = open(filename,"r")#,encoding='utf-8')

#each line is a string


comment_re = re.compile(r'^ *#') #string starts with zero or more " ", then a #


time_series = []
for line in f:
#need a regex to catch the comment line
#make list of comment chars, check if line starts with it	
	if re.match(comment_re,line):
		print("comment line")
	else:
		value = float(line.split()[column])
		print(value)
		time_series.append(value)

#print(data.split())
# for line in data.split():
# 	print(line)

f.close()
#1st step: read file, just output a single column
#Need parser library, argparse is the current one

#Ingredients:
#Need to read the file, first with \t as separator, then with several
#Input of columns: Ideal would be command line: if 1 number is input, just do that mumber, if 2 numbers: do the quotient
#Just plot the time series
#Select the starting and end point for blocking -> command line or interface
#do the actual blocking: select product of small integers, etc.
#show plateau graph, user can then select
#Later, make it interactive

