#!/usr/bin/python
import itertools
import csv

# csvFileName = 'DYCD_after-school_programs.csv'
csvFileName = "NYC_City_Hall_Library_Publications.csv"
numberRecords = 0
min_sup = 0.3
min_conf = 0.8
LList = []	#list of L1,L2,...,Lk

# Build initial dictionary
def initDict(file):
    #define a temporary dictionary to calculate the number of appearance of EACH ITEM <item, list of appearing records no.>
    initDict = {}
    global numberRecords
    
    csvreader = csv.reader(file.read().splitlines(), delimiter=",")
    #TO-DO:
    # Pay attention to the first line of csv , spaces 
    for row in csvreader:
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
    
# Main a-priori algorithm
def aprioriAlg():
	global LList
	global numberRecords
	global min_sup
	k = 2
	while len(LList) >= k - 1:
	# while k == 2:
		#the number of L and the position it is stored in LList has a difference 1. e.g. L2 is stored in LList[1]
		Lk_1 = LList[k - 1 - 1]
		#Get new candidates set [<"pen, int", [1,2,6,9,56,...]>,<"...", [....]>,<...>,...]
		Ck = Apriori_Gen(Lk_1)
		#check if the candidate with a larger support than min_sup
		Lk = {}
		for key in Ck.keys():
			if(float(len(Ck[key])) / numberRecords >= min_sup):
				Lk[key] = Ck[key]
		#add Lk to the global LList if it is not empty
		if len(Lk.keys()) != 0:
			LList.append(Lk)
		k += 1

# Used for Join procedure in a-priori gen 
# Check if p,q differ only in the last word
# Check if b's last element >  a's last element dictionary order, numeric order, etc.
def diff(a,b):
	for i in range(len(a)-1):
		if(a[i]!=b[i]):
			return False
	if(a[len(a)-1] < b[len(a) - 1]):
		return True

# Given oldwords' transactions list, and newly append word
# return the intersaction of transactions
def merge(L,oldwords,word):
	global LList
	L1 = LList[0]
	oldList = L[oldwords]
	tmpList = L1[word]
	return list(set(oldList).intersection(set(tmpList))) 

# Apriori gen algorithm
# return candidate set
def Apriori_Gen(L):
	C = {};
	keys = []
	for k in L.keys():
		keys.append(k.split(';'))
	#Join procedure
	for p in keys:
		for q in keys:
			if(p!=q):
				# check if p,q differ only in the last word
				if(diff(p,q)):
					newItem = p[:]
					newItem.append(q[len(q)-1])
					# prune stage
					if(prune(keys,newItem)):
						# Merge the transactions number in common
						C[';'.join(newItem)] = merge(L , ';'.join(p), q[len(q)-1])
	return C

# Prune stage
# Check newItem in Candidate's subsets are contained in L[k-1]
def prune(keys, newItem):
	# subset of length k-1 
	for subitem in list(itertools.combinations(newItem, len(newItem)-1)):
		if sorted(list(subitem)) not in keys:
			return False
	return True

# Association Rule Generation
def Rule_gen():
	global LList
	global min_conf
	global numberRecords
	L1 = LList[0]

	Rule = {}
	prevLk = {}
	for Lk in LList:
		for key in Lk:
			freqItem = key.split(';')
			if(len(freqItem)!=1):
				for i in range(len(freqItem)):
					temp = freqItem[:]
					RHS = temp.pop(i)
					RHSList = L1[RHS]
					LHS = ';'.join(temp)
					LHSList = prevLk[LHS]
					if(Conf(LHSList,RHSList) >= min_conf):
						print LHS, " => ", RHS, "conf:", Conf(LHSList,RHSList), "sup:", float(len(Lk[key]))/numberRecords
						Rule[LHS] = RHS
		prevLk = Lk
	return Rule
# Given the LHS, RHS, compute the confidency
def Conf(LHSList,RHSList):
	intesectLen = len(set(LHSList).intersection(set(RHSList)))
	LHSLen = len(LHSList)
	return float(intesectLen)/LHSLen

def main():
    global LList
    global csvFileName
    global min_sup
    global numberRecords
    #open CSV file
    file = open(csvFileName,'r')
    #read the file and build a 1-element-key dictionary with value be the number of appearance
    dictionary = initDict(file)
    file.close()

    #get L1 from C1
    L1 = {}
    for item in dictionary.keys():
        # check if support meets min_sup
        if float(len(dictionary[item])) / numberRecords >= min_sup:
            L1[item] = dictionary[item]
    #add L1 to the L list
    LList.append(L1)
    aprioriAlg()
	# From LList to generate the association 
    Association_Rule = Rule_gen()

    # # Print the result
    # for key in Association_Rule:
    # 	print key.split(";"), " => ", Association_Rule[key], "conf:", 

if __name__ == "__main__":
    main()