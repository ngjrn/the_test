#!/usr/bin/python

import sys
import random
import hashlib

h=hashlib.sha1()

def usage():
	print('usage: '+sys.argv[0]+' [ed] password')

if len(sys.argv)!=3:
	usage()
	exit(1)
	
if sys.argv[1]!='e' and sys.argv[1]!='d':
	usage()
	exit(1)
	
h.update(sys.argv[2].encode('utf8'))
the_seed=0

for d in h.digest():
	the_seed*=256
	the_seed+=d

rng=random.Random()
rng.seed(the_seed)

data=sys.stdin.read(-1)

transposition=[]

for i in range(0, len(data)):
	p=rng.randint(0,len(data)-1)
	transposition.append((min(i,p),max(i,p)))

if sys.argv[1]=='d':
	transposition.reverse()
	
for tr in transposition:
	if (tr[0]==tr[1]):
		continue
	
	a=data[tr[0]]
	b=data[tr[1]]
	
	data=data[:tr[0]]+b+data[tr[0]+1:tr[1]]+a+data[tr[1]+1:]
	
sys.stdout.write(data)