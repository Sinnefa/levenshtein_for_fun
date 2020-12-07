##############################################
# My implementation Levenshtein distance
# Recursion https://en.wikipedia.org/wiki/Levenshtein_distance
##############################################
lev = lambda a,b: len(a) if len(b)==0 else len(b) if len(a)==0 else lev(a[1:],b[1:]) if a[0]==b[0] else 1+min(lev(a[1:],b),lev(a,b[1:]),lev(a[1:],b[1:]))

