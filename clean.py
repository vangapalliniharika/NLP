from sys import argv
#import nltk
import re
script, filename = argv
i=1
txt = open(filename)
for j in txt:
	lis = j.split()
	num = lis[1]
       # print "number is ",num
       # print "i is ",i
	if (int(num) >= i):
         #      print "number and i is" ,(int(num),i)
		data =  " ".join(lis[2:])
		data = re.sub('[!@#$,\.\)\(\:\;\"?\-\'%&*\/]', '', data)
		data = data.split()
         #       print "Data[-1] is",data[-1]
		if  int(data[-1]) == 4:
			data[-1] = "1"
			print " ".join(data)
		elif( int(data[-1]) == 0):
			data[-1] = "0"
			print " ".join(data)

		i = i+1
