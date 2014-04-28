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

def prune(key):
	return True

def diff(a,b):
	for i in range(len(a)-1):
		if(a[i]!=b[i]):
			return False
	if(a[len(a)-1] < b[len(a) - 1]):
		return True

def merge(L,oldwords,word):
	global LList
	L1 = LList[0]
	oldList = L.get(oldwords)
	tmpList = L1.get(word)
	return list(set(oldList+tmpList)) 

def Apriori_Gen(L):
	C = {};
	for k1 in L.keys():
		p = k1.split(",")
		for k2 in L.keys():
			q = k2.split(",")
			if(p!=q):
				if(diff(p,q)):
					key = p
					key.append(q[len(q)-1])
					if(prune(key)):
						C[key] = merge(L,p,q[len(q)-1])
	return C

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