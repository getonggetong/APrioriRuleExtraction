import csv

# global dictionary
dic = {}
csvfname = 'DYCD_after-school_programs.csv'
num_records = 0
reader = None 
result = []

####### functions #######

def readCSV():
	return open(csvfname)

def buildDic(csvfile):
	global dic
	global num_records
	global reader 
	reader = csv.reader(csvfile.read().splitlines(), delimiter=",")
	for row in reader:
		# caution: a row doesn't contain same item more than once
		num_records += 1
		for item in row:
			if(item not in dic.keys()):
				dic[item] = 1
			else:
				dic[item] = dic[item]+1

def apriori_gen(L):
	pass	

def Apriori(L):
	global reader
	global result

	nL = L
	while nL!=None:
		C = apriori_gen(nL)

		for row in reader:
			# Find all the supported itemsets with size k in C
			# C_t = subset(C_k, t)
			# forall candidates c \in C_t
				# c.count++
		# end

		# nL = {c \in C_k | c.count >= min_sup}
	# end

	# return 

def supportFilter(min_sup):
	#according to the threshold, filter the dictionary 
	global dic
	global num_records

	FilteredDict = []

	for key in dic.keys():
		dic[key] = dic[key]/num_records
		if(dic[key] >= min_sup):
			FilteredDict.append(key)

	return FilteredDict


# get input 

def main():
	#readCSV
	f = readCSV()
	#for each row, count the words and its frequency 
	buildDic(f)
	L = supportFilter(0.5)
	Apriori(L)
	#calculate the support


#Entry
if __name__ == "__main__":
	main()