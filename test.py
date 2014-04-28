#!/usr/bin/python

def apriori_gen(L):
	# Join
	
	# Prune
	pass	

def prune(key):
	return True

def diff(a,b):
	for i in range(len(a)-1):
		if(a[i]!=b[i]):
			return False
	if(a[len(a)-1] < b[len(a) - 1]):
		return True

def merge(L,oldwords,word):
	global L1
	oldList = L.get(oldwords)
	tmpList = L1.get(word)
	return list(set(oldList+tmpList)) 

def Apriori(L):
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

L1 = {"a":[0,3],"b":[0,1],"c":[0,1,2],"d":[0,1,2,3]}
L2 = {"a,c":[0,2], "a,b":[0,3],"a,d":[0,2,3],"b,d":[0,1,3],"c,d":[0,1,2],"b,c":[0,1]}

Apriori(L2)
