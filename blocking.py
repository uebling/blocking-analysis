#!/usr/bin/python
'''

blocking.py [options] filename

Text here.'''

#from math import sqrt
import argparse
import re
#import os
#import sys

def parse():
	parser = argparse.ArgumentParser()
	# #Lots of options for add_argument, check documentation..., especially 'action'
	parser.add_argument("filename",type=str,help='filename for the data')
	parser.add_argument("-d","--data",type=int,default=[],action='append',help="Specify columns")
	parser.add_argument("-s","--start",type=int,default=1,help="Data point to start blocking")
	parser.add_argument("-e","--end",type=int,default=0,help="Data point to end blocking")

	return parser.parse_args()

class Blocking():

	def __init__(self,filename,columns,start,end):

		self.filename = filename
		self.columns = columns
		self.start = start
		self.end = end
		self.delimiters = ["\t"," ",","]
		self.comment_re = re.compile(r'^ *#')

	def prepare_data(self):
		f = open(filename,"r")#,encoding='utf-8')
		time_series = []
		for line in f:
		#need a regex to catch the comment line
		#make list of comment chars, check if line starts with it	
			if re.match(self.comment_re,line):
				print("comment line")
			else:
				#Change so that it prepares several columns
				value = float(line.split()[self.columns[0]])
				print(value)
				time_series.append(value)

		f.close()



	def ask_input():
		pass

	def show_data():
		pass


options = parse()
filename = options.filename
stuff = Blocking(filename,options.data,options.start,options.end)
stuff.prepare_data()


#print(data.split())
# for line in data.split():
# 	print(line)

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

# if __name__ == '__main__':
# 	main()