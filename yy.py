import csv

with open('straightcsv.csv', 'rb') as csvfile:
		rowreader = csv.reader(csvfile, dialect='excel', quotechar='`')
		for row in rowreader:
			print row