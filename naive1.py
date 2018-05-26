from __future__ import division 
from sys import argv
from nltk.corpus import stopwords
import math
script, word = argv
i=1
#stop = stopwords.words("english")
pos = open('pos.txt','r')
neg = open('neg.txt','r')
voca = open('vocabluary.txt','r')


def populate(filed):
	voc = []
	for i in filed:
        	i = i.split()
		voc = voc + i
        #print voc
	return voc

def prob(word,lis):
	k = (lis.count(word) + 1)/(len(lis) + len(set(lis)))
	#print lis.count(word)
        #print lis.count(word)+1
        #print len(set(lis))
	#print (len(lis) + len(set(lis)))
	#print k
        #print math.log10(k)
	return math.log10(k)

def classify(stri,posi,negi):
	stri = stri.split()
        #print stri
	nprob = 0
	pprob = 0
	for i in stri:
	       # print i
        	nprob = nprob + prob(i,negi)
		pprob = pprob + prob(i,posi)
	if(nprob > pprob):
		print ('Negative(-)')
	else:
		print ('Positive(+)')
			

vocab = populate(voca)
positive = populate(pos)
negative = populate(neg)
classify(word,positive,negative)	

