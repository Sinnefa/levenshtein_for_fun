import textdistance
from sickLevenshtein import *
from levenstheinDP import *
from recursiveLevensthein import *
import random
import time

print("Levenshtein package\tTIME Levenshtein package\tRecursive\tTIME Recursive\tMy memroy optimized Levenshtein\tTIME My memroy optimized Levenshtein\tMy sick Levenshtein\tTIME My sick Levenshtein")
for i in range(100):
	a = ''.join(random.choices(["a","c","t","g"], k = random.randint(2,10)))
	b = ''.join(random.choices(["a","c","t","g"], k = random.randint(2,10)))
	# Levenshtein package
	start_time = time.time()
	d1 = textdistance.levenshtein(a,b)
	t1 = time.time() - start_time
	# Levenshtein recursive lambda
	start_time = time.time()
	d2 = lev(a,b)
	t2 = time.time() - start_time
	# My memroy optimized Levenshtein
	start_time = time.time()
	d3 = myld(a,b)
	t3 = time.time() - start_time
	# My sick Levenshtein
	start_time = time.time()
	d4 = sickLevenshtein(a,b)
	t4 = time.time() - start_time
	print(str(d1)+"\t"+str(t1)+"\t"+str(d2)+"\t"+str(t2)+"\t"+str(d3)+"\t"+str(t3)+"\t"+str(d4)+"\t"+str(t4)+"\t"+a+"\t"+b)
	#print(d1==d4)
