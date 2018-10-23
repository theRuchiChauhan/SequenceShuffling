"""
Implemetation of segment shuffling method

Algorithm :
To shuffle an array a of n elements (indices 0..n-1):
  for i from n − 1 downto 1 do
       j ← random integer with 0 ≤ j ≤ i
       exchange a[j] and a[i]
================================================
Author: Ruchi Chauhan
Date of Original Version: 23 Oct 2018
================================================
"""
import numpy as np
import random
import sys
import pdb

def readSequence(fname):
	f = open(fname, 'r')
	seq = f.readline().strip('\n')
	print('\n' + 
	seq)
	return seq

def displayCount(sequence):
	freqDict = {}
	for char in sequence:
		if (char in freqDict):
			freqDict[char]+=1
		else:
			freqDict[char]=1
	for key in sorted(freqDict.keys()):
		print(key + ':' + str(freqDict[key])+' ', end='')

def segShuffle(seqList):
	for i in reversed(range(1, m)):				#pick an element in seqList[:i+1] with which to exchange seqList[i]
		j = random.randint(0,i+1)
		seqList[i], seqList[j] = seqList[j], seqList[i]
	segmentSeq = "".join(seqList)
	print('\n' + segmentSeq)
	return segmentSeq

def createSegments(x):
	seqList = []
#	pdb.set_trace()
	for i in range(0,n,x):
		seg = seq[i:i+x]
		seqList.append(seg)
	#print(seqList)
	return seqList

fname = sys.argv[1]
segSize = int(sys.argv[2])
seq = readSequence(fname)
n = len(seq)
displayCount(seq)
seqList = createSegments(segSize)
m = len(seqList)
segmentSeq = segShuffle(seqList)
displayCount(segmentSeq)
print('\n')

################################################## Code Dump #######################################
	#for key, value in freqDict.items():
		#print (key, value)
	#print(freqDict.items())
