import csv

# global dictionary
dic = {}
csvfname = 'DYCD_after-school_programs.csv'
num_records = 0
csvreader = None 
result = []

####### functions #######

def readCSV():
	return open(csvfname)

def buildDic(csvfile):
	global dic
	global num_records
	global csvreader 
	csvreader = csv.reader(csvfile.read().splitlines(), delimiter=",")
	for row in csvreader:
		# caution: a row doesn't contain same item more than once
		num_records += 1
		for item in row:
			if(item not in dic.keys()):
				dic[item] = 1
			else:
				dic[item] = dic[item]+1

def apriori_gen(L):
	# Join
	
	# Prune

	pass	

def Apriori(L):
	global reader
	global result

	# nL = L
	# while nL!=None:
	# 	C = apriori_gen(nL)

	# 	for row in reader:
	 		# Find all the supported itemsets with size k in C
			# C_t = subset(C_k, t)
			# forall candidates c \in C_t
				# c.count++
		# end

		# nL = {c \in C_k | c.count >= min_sup}
	# end

	# return 

def filter(threshold, L):
	global num_records
	global csvreader
	Fl = []
	for row in csvreader:
		# if this row contains 
		pass


def supportFilter(sup_thre):
	#according to the threshold, filter the dictionary 
	global dic
	global num_records

	FilteredDict = []

	for key in dic.keys():
		dic[key] = dic[key]/num_records
		if(dic[key] >= sup_thre):
			FilteredDict.append(key)

	# Ensure it's sorted
	return FilteredDict.sort()


# get input 

def main():
	global num_records
	min_sup = 0.5
	#readCSV
	f = readCSV()
	#for each row, count the words and its frequency 
	buildDic(f)
	# Generate L_1
	L = filter(min_sup, dic)

	Apriori(L)
	#calculate the support


#Entry
if __name__ == "__main__":
	main()