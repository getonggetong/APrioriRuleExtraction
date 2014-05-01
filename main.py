#!/usr/bin/python
import itertools
import csv

csvFileName = 'sample.csv'
numberRecords = 0
min_sup = 0.5
min_conf = 0.9
LList = []#list of L1,L2,...,Lk

#build initial dictionary
def initDict(file):
    #define a temporary dictionary to calculate the number of appearance of EACH ITEM <item, list of appearing records no.>
    initDict = {}
    global numberRecords
    
    csvreader = csv.reader(file.read().splitlines(), delimiter=",")
    #TO-DO:
    # Pay attention to the first line of csv , spaces 
    # 
    for row in csvreader:
    	print "row: ",row
        for item in row:
        	# eliminate the space
        	if item != '':
	            if(item not in initDict.keys()):
	                initDict[item] = [numberRecords]
	            elif(numberRecords not in initDict[item]):
	            	# Check for duplicate row number
	                initDict[item].append(numberRecords)
        #increase the number of records by one for further support/confidence calculation 
        numberRecords += 1
    
    return initDict
    
def aprioriAlgo():
	global LList
	global numberRecords
	global min_sup
	L1 = LList[0]
	k = 2
	while len(LList) >= k - 1:
	# while k == 2:
		#the number of L and the position it is stored in LList has a difference 1. e.g. L2 is stored in LList[1]
		Lk_1 = LList[k - 1 - 1]
		#Get new candidates set [<"pen, int", [1,2,6,9,56,...]>,<"...", [....]>,<...>,...]
		print "L k-1:", Lk_1
		Ck = Apriori_Gen(Lk_1)
		print "Candidate:", Ck
		#check if the candidate with a larger support than min_sup
		Lk = {}
		for key in Ck.keys():
			if(float(len(Ck[key])) / numberRecords >= min_sup):
				Lk[key] = Ck[key]

		print "Lk:", Lk
		#add Lk to the global LList if it is not empty
		if len(Lk.keys()) != 0:
			LList.append(Lk)
		k += 1

	print "LList", LList

# Compare a,b if only the last element differs 
def diff(a,b):
	for i in range(len(a)-1):
		if(a[i]!=b[i]):
			return False
	if(a[len(a)-1] < b[len(a) - 1]):
		return True

# Merge list 
def merge(L,oldwords,word):
	global LList
	L1 = LList[0]
	print "oldwords: ", oldwords
	print "word: ",word
	oldList = L[oldwords]
	tmpList = L1[word]

	return list(set(oldList).intersection(set(tmpList))) 

# Apriori algorithm
def Apriori_Gen(L):
	C = {};
	keys = []
	for k in L.keys():
		keys.append(k.split(','))

	print "keys :" , keys
	#Join 
	for p in keys:
		for q in keys:
			if(p!=q):
				# test if p,q differ only in the last word
				if(diff(p,q)):
					print "p:", p
					print "q:", q
					newItem = p[:]
					newItem.append(q[len(q)-1])
					print "new Item : ", newItem
					# prune stage
					if(prune(keys,newItem)):
						# Merge the transactions in common
						C[','.join(newItem)] = merge(L , ','.join(p), q[len(q)-1])
	return C

def prune(keys, newItem):
	# subset of length k-1 
	for subitem in list(itertools.combinations(newItem, len(newItem)-1)):
		if sorted(list(subitem)) not in keys:
			return False
	return True

def main():
    global LList
    global csvFileName
    global min_sup
    global numberRecords

    #open CSV file
    file = open(csvFileName)
    #read the file and build a 1-element-key dictionary with value be the number of appearance
    dictionary = initDict(file)
    print "dictionary:", dictionary
    #get L1 from C1
    L1 = {}
    for item in dictionary.keys():
        # check if support meets min_sup
        if float(len(dictionary[item])) / numberRecords >= min_sup:
            L1[item] = dictionary[item]

    print "L1: ",L1
    #add L1 to the L list
    LList.append(L1)

    aprioriAlgo()

if __name__ == "__main__":
    main()