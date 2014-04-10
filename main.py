import csv

with open('a.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    for row in spamreader:
	        print ', '.join(row)