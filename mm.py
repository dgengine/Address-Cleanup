#################################################################################
# Python script:  mm.py
# This script takes a comma delimited export from Firehouse software in .CSV and divides
# the resulting list of addresses into three separate data files to be GeoCoded in ArcGIS
# It accounts for a common address like '8420 Hardwicke Dr.'
# It accounts for an intersection, intersection type of location
# It accounts for a Lat.,Long pair as well.
# It does NOT account for a X hundred block location
#
# Script coded by David Croll Community Development Department for the City of Johnston
# Script coded on 12/11/2016
# Script last modified on 12/12/2016
#
#
import re

foS = open("ArcgisTable.csv")
#fileout = open("LatLong.dat","w")
fileout2 = open("Addrout.txt","w")
fileout3 = open("Intout.dat","w")

###############################################################################
# FUNCTION for removal of quotes                                              #
def remquote(firstsearchable):
	if firstsearchable[0] == '"':
		firstsearchable = firstsearchable[1:]
	else:
		firstsearchable = firstsearchable
	return firstsearchable
###############################################################################
###############################################################################
# FUNCTION for finding Intersection & Intersection                            #
def intersearch(firstsearchable):
	if '&' in firstsearchable:
		firstsearchable = firstsearchable
	else:
		firstsearchable = "NOT HERE"
	return firstsearchable
#
###############################################################################
counter = 0
counter2 = 0
data_list = []
#newlist = []
#address = []
#splitlist = []
#x = []
#y = []
#z = []
with foS as f:
    for line in f:
		counter = counter + 1
		datalist = line.split(",")
		#print datalist[0]
		#address = data_list
		#print address
		#line.split(",")
		#print data_list[-5]
		#Lat = data_list[10]
		#Long = data_list[11]
		#newlist = data_list
		#address = newlist[6]
		#print address
#		splitlist = str(address.split("/"))
#		splitlist = address.split("/")
		#print splitlist
#		fmtsplitlist = address.split("/")
		match = re.search(r'(-B)', datalist[0])
#		lengthlist = len(data_list)
		if match:
			counter2 = counter2 + 1
			print datalist
#			if Lat == '0':
#				x = remquote(address)
#				y = x.split("/")
#				z = intersearch(y[0])
#				if z == "NOT HERE":
#					fileout2.write(y[0] + ',\n')
#				else:
#					fileout3.write(z + '\n')
#				print address
#			else:
				#print len(split_list)
#				fileout.write(Lat + ',' + Long+ '\n')
#		elif lengthlist == 13:
#			Lat = data_list[11]
#			Long = data_list[12]
#			if Lat == '0':
#				x = remquote(address)
#				y = x.split("/")
#				z = intersearch(y[0])
#				if z == "NOT HERE":
#					fileout2.write(y[0] + ',\n')
#				else:
#					fileout3.write(z + '\n')
#								
#			else:
				#print len(data_list)
#				fileout.write(Lat + ',' + Long+ '\n')								
#		else:
#			Lat = data_list[12]
#			Long = data_list[13]
#			if Lat == '0':
#				x = remquote(splitlist)
#				y = x.split("/")
#				z = intersearch(y[0])
#				if z == "NOT HERE":
#					fileout2.write(y[0] + ',\n')
#				else:
#					fileout3.write(z + '\n')
#
#			else:
#				fileout.write(Lat + ',' + Long+ '\n')
###################################################################
print counter
print counter2
foS.close
#fileout.close
fileout2.close
fileout3.close