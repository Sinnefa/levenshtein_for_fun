# Levenshtein implementations for fun
## My quest to one-line implementation
I wanted to implement the Levenshtein algorithms (Dynamic programming) in one line.
Here it is:

```python
##############################################
# My sick implementation Levenshtein distance
# Dynamic Programming in one line
##############################################
def sickLevenshtein(a,b):
	return (lambda count,m,f: f(count,m,f))(0,[[c if r==0 else r if c==0 else 0 for c in range(len(a)+1)] for r in range(len(b)+1)],lambda count,m,f: [m:=f(count+1,[[m[i][j] if i==0 or j==0 else min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+(a[j-1]!=b[i-1])) for j in range(len(a)+1)] for i in range(len(b)+1)],f)[0] if count<len(a)*len(b) else m])[0][len(b)][len(a)]
```

I also implemented it with the naive recursive mathemtical definition https://en.wikipedia.org/wiki/Levenshtein_distance and the standard DP memory optimized version. In memory optimized you keep only two lines. I also wrote a script to compre my implementations agains a standard implementation contained in the package "python-Levenshtein"
