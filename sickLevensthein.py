##############################################
# My sick implementation Levenshtein distance
# Dynamic Programming in one line
##############################################
def assigner(a,b):
	a[:]=b[:]
	return a

def mySickLevenshtein(a,b):
	# Depends on assigner() as
	# you can't assign within in-line loops
	return [[assigner(v1,[assigner(v2,[v2[0]]+[min(v2[i-1]+1,v1[i]+1,v1[i-1]+(b[i-1]!=a[v2[0]-1])) for i in range(1,len(b)+1)]) for i in range(1,len(b)+1)][-1]) for v2 in [[i]+[0 for i in range(0,len(b)+1)][1:] for i in range(1,len(a)+1)]] for v1 in [list(range(0,len(b)+1))]][-1][-1][-1]
