#!/usr/bin/python
import itertools
import csv

csvFileName = 'DYCD_after-school_programs.csv'
numberRecords = 0
min_sup = 0.4
min_conf = 0.9
LList = []#list of L1,L2,...,Lk

#build initial dictionary
def initDict(file):
    #define a temporary dictionary to calculate the number of appearance of EACH ITEM <item, list of appearing records no.>
    initDict = {}
    global numberRecords
    
    csvreader = csv.reader(file.read().splitlines(), delimiter=",")
    for row in csvreader:
        #increase the number of records by one for further support/confidence calculation 
        numberRecords += 1
        #
        for item in row:
            if(item not in initDict.keys()):
                initDict[item] = [numberRecords]
            else:
                initDict[item].append(numberRecords)
    
    return initDict
    
    
def aprioriAlgo():
	global LList
	L1 = LList[0]
	k = 2
	while len(LList) >= k - 1:
		#the number of L and the position it is stored in LList has a difference 1. e.g. L2 is stored in LList[1]
		Lk_1 = LList[k - 1 - 1]
		#get new candidates set [<"pen, int", [1,2,6,9,56,...]>,<"...", [....]>,<...>,...]
		Ck = Apriori_Gen(Lk_1)
		k += 1

# Compare a,b if only the last element differs 
def diff(a,b):
	for i in range(len(a)-1):
		if(a[i]!=b[i]):
			return False
	if(a[len(a)-1] < b[len(a) - 1]):
		return True

# Merge list 
def merge(L,oldwords,word):
	global L1
	oldList = L[oldwords]
	tmpList = L1[word]

	return list(set(oldList).intersection(set(tmpList))) 

# Apriori algorithm
def Apriori(L):
	C = {};
	keys = []
	for k in L.keys():
		keys.append(k.split(','))

	#Join 
	for p in keys:
		for q in keys:
			if(p!=q):
				# test if p,q differ only in the last word
				if(diff(p,q)):
					newItem = p[:]
					newItem.append(q[len(q)-1])
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
    #get L1 from C1
    L1 = {}
    for item in dictionary.keys():

        # check if support meets min_sup
        if float(len(dictionary[item])) / numberRecords >= min_sup:
            L1[item] = dictionary[item]
    #add L1 to the L list
    LList.append(L1)
    print L1

if __name__ == "__main__":
    main()