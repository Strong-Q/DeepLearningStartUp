#!/usr/bin/python3

from collections import Counter

words1 = open("./happiness_seg.txt", encoding="utf8").read().split(' ')

words2 = []

punc = ['。','，','“','”','...','-','？','！','、','；','（','）','：','?',]

for i in range(len(words1)-1):
	if words1[i] in punc or words1[i+1] in punc :		
		continue
	else:		
		words2.append(words1[i]+" "+words1[i+1])

print (Counter(words2).most_common(10))		
		
