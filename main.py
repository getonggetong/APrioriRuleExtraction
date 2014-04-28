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
    #for (k = 2; Lk_1 != null; k++):
    k = 2
    while len(LList) >= k - 1:
        #the number of L and the position it is stored in LList has a difference 1. e.g. L2 is stored in LList[1]
        Lk_1 = LList[k - 1 - 1]
        Ck = apriori_gen(Lk_1)#get new candidates set [<"pen, int", [1,2,6,9,56,...]>,<"...", [....]>,<...>,...]
        # for each itemset in Ck

        k += 1



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

    # aprioriAlgo()


    
if __name__ == "__main__":
    main()