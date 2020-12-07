##############################################
# My implementation Levenshtein distance
# Dynamic Programming
##############################################
def step(str,c,v1,v2):
	for i in range(1,len(str)+1):
		v2[i]=min(v2[i-1]+1,v1[i]+1,v1[i-1]+(str[i-1]!=c))
	return v2

def myld(a,b):
	v1 = list(range(0,len(b)+1))
	for i in range(1,len(a)+1):
		v2 = [0 for i in range(0,len(b)+1)]
		v1=step(b,a[i-1],v1,[i]+v2[1:]).copy()
	return v1[-1]
