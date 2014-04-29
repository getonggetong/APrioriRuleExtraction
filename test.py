#!/usr/bin/python
import itertools
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

L1 = {"a":[0,3],"b":[0,1],"c":[0,1,2],"d":[0,1,2,3]}
# L2 = {"a,c":[0,2], "a,b":[0,3],"a,d":[0,2,3],"b,d":[0,1,3],"c,d":[0,1,2],"b,c":[0,1]}
L2 = {"a,c":[0,2], "a,b":[0,3]}

KEYS = [['a','b'],['a','c'],['b','c']] 
Item = ['a','b','c']
print(prune(KEYS,Item))

# Apriori(L2)
