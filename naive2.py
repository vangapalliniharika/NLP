from sys import argv
from nltk.corpus import stopwords
import math
script, word = argv
script, number = argv
i=1
stop = stopwords.words("english")
pos = open('pos.txt','r')
neg = open('neg.txt','r')
voca = open('vocabluary.txt','r')


#pos = open('pos.txt','w')
#neg = open('neg.txt','w')
#voca = open('vocabluary.txt','w')
#j = number
def create(number):
        #print number
	j = int(number)
	j = (j+1) % 10
	pos = []
	neg = []
	voab = []
	while(j != int(number)):
		print "learning file",j
		fil = open(str(j),'r')
		for line in fil:
			lis = line.split()
			if (lis[-1] == '1'):
				pos = pos + lis[:-1]
			else:
				neg = neg + lis[:-1]
			for word in line:
				if (word not in voab and (word != "1" or word != "0")):
					voab.append(word)
		j = (j+1)%10
		fil.close()
	return (pos,neg,voab)
def prob(word,lis):
	k = (lis.count(word) + 1)/(len(lis) + len(set(lis)))
        return math.log10(k)
def populate(filed):
 	voc = []
        nprob=0
        pprob=0
 	for i in filed:
       # def classify(stri,posi,negi):
 		nprob = nprob + prob(i,negi)
 		pprob = pprob + prob(i,posi)
 	if(nprob > pprob):
		print ('-')
		return '0'
 	else:
		print ('+')
			
		return '1'

def validation(number):			
	positive,negative,vocab = create(number)
	#print positive
#vocab = populate(voca)
#positive = populate(pos)
#negative = populate(neg)
	TP = 0
	count = 0;
	test = open(number,'r')
	for line in test:
		#print line
		li = line.split()
		li = li[:-1]
		linee = " ".join(li)
	#	print linee
		res = classify(linee,positive,negative)	
		lis = line.split()
	#	print "checking",lis[-1],res
		if (lis[-1] == res):
		     TP = TP + 1
		count = count + 1
	print (TP/count)*100
 	
validation(number)
			
