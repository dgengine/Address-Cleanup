#################################################################################
# Python script:  firefinal.py
# This script takes a comma delimited export from Firehouse software and divides
# the resulting list of addresses into three separate data files to be mapped in ArcGIS
# It accounts for a common address like '8420 Hardwicke Dr.'
# It accounts for an intersection, intersection type of location
# It accounts for a Lat.,Long pair as well.
# It does NOT account for a X hundred block location
#
# Script coded by David Croll Community Development Department for the City of Johnston
# Script coded on 12/09/2016
# Script last modified on 12/12/2016
#
#
import re
#
foS = open("jgfd1516.csv")
fileout = open("LatLong.dat","w")
fileout2 = open("Addrout.txt","w")
fileout3 = open("Intout.dat","w")
counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
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
data_list = []
newlist = []
address = []
splitlist = []
x = []
y = []
z = []
with foS as f:
    for line in f:
		counter = counter +1
		line = line.strip()
		data_list = line.split(",")
		Lat = data_list[-2]
		Long = data_list[-1]
		newlist = data_list
		address = newlist[9]
#		print counter
#		print data_list
#		print Long
#		print newlist
#		print address
#		splitlist = str(address.split("/"))
		splitlist = address.split("/")
#		print splitlist
#		fmtsplitlist = address.split("/")
#		match = re.search(r'(\w+) (\w+) (\w+)', splitlist)
		lengthlist = len(data_list)
#		print lengthlist
		if lengthlist == 15:
			counter1 = counter1 + 1
			if Lat == '0':
				x = remquote(address)
##				y = x.split("/")
				z = intersearch(y[0])
##				if z == "NOT HERE":
##					counter2 = counter2 + 1
##					fileout2.write(y[0] + ',\n')
				else:
					counter3 = counter3 + 1
##					fileout3.write(z + '\n')
					print address
			else:
#				print len(split_list)
				counter4 = counter4 + 1
				print 'Lat_Long out'
##				fileout.write(Lat + ',' + Long+ '\n')
		elif lengthlist == 16:
			Lat = data_list[-2]
#			Long = data_list[-1]
			if Lat == '0':
				x = remquote(address)
				print x
				y = x.split("/")
				print y
				z = intersearch(y[0])
				print z
##				if z == "NOT HERE":
					counter2 = counter2 + 1
##					fileout2.write(y[0] + ',\n')
				else:
					counter3 = counter3 + 1
					Print 'Else Out'
##					fileout3.write(z + '\n')
#								
			else:
				print 'Lat_Long out'
#				print len(data_list)
				counter4 = counter4 + 1
##				fileout.write(Lat + ',' + Long+ '\n')								
		else:
			Lat = data_list[-2]
#			Long = data_list[-1]
			if Lat == '0':
				x = remquote(splitlist)
				y = x.split("/")
				z = intersearch(y[0])
				if z == "NOT HERE":
					counter2 = counter2 + 1
##					fileout2.write(y[0] + ',\n')
				else:
					counter3 = counter3 + 1
##					fileout3.write(z + '\n')
#
			else:
				counter4 = counter4 + 1
				print 'Lat_Long out'
##				fileout.write(Lat + ',' + Long+ '\n')
##################################################################
#
###################################################################
print counter
print counter1
print counter2
print counter3
print counter4
foS.close
fileout.close
fileout2.close
fileout3.close