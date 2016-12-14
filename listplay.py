import re
foS = open("DataIn2.csv")
#fileout = open("DavidOut","w")
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

with foS as f:
    for line in f:
		line = line.strip()
		data_list = []
		parsedline = []
		begline = []
		endline = []
		midline = []
		puttogether = []
		data_list = line
		parsedline = line.split(",")
		LL = len(parsedline)
		if LL == 13:
			begline = parsedline[:7]
			midline = parsedline[7]
			endline = parsedline[-5:]
			puttogether = begline += midline
			print begline
			print midline
			print endline
			print puttogether
			print parsedline
		elif LL == 14:
			begline = parsedline[:7]
			midline = parsedline[7:9]
			endline = parsedline[-5:]
			print '***********************'
			print begline
			print midline
			print endline
			print '***********************'
		elif LL == 15:
			begline = parsedline[:7]
			midline = parsedline[7:10]
			endline = parsedline[-5:]
			print '***********************'
			print begline
			print midline
			print endline
			print '***********************'
		elif LL == 16:
			begline = parsedline[:7]
			midline = parsedline[7:11]
			endline = parsedline[-5:]
			print '***********************'
			print begline
			print midline
			print endline
			print '***********************'
		else:
			begline = parsedline[:7]
			midline = parsedline[7:12]
			endline = parsedline[-5:]
			print '***********************'
			print begline
			print midline
			print endline
			print '***********************'
##################################################################
# TO DO LIST:
#
#  
###################################################################
foS.close
#fileout.close
#fileout2.close
#fileout3.close
