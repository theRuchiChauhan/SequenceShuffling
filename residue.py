"""
Implemetation of Residue shuffling method [Fisher–Yates method with Durstenfeld's version]

Algorithm :
To shuffle an array a of n elements (indices 0..n-1):
  for i from n − 1 downto 1 do
       j ← random integer with 0 ≤ j ≤ i
       exchange a[j] and a[i]
================================================
Author: Ruchi Chauhan
Date of Original Version: 22 Oct 2018
================================================
"""
import numpy as np
import random
import sys

def readSequence(fname):
	f = open(fname, 'r')
	seq = f.readline().strip('\n')
	print(seq)
	return seq

def resShuffle(seqList):
	for i in reversed(range(1, n)):				#pick an element in seqList[:i+1] with which to exchange seqList[i]
		j = random.randint(0,i+1)
		seqList[i], seqList[j] = seqList[j], seqList[i]
	residueSeq = "".join(seqList)
	print(residueSeq)
	return residueSeq

def displayCount(sequence):
	freqDict = {}
	for char in sequence:
		if (char in freqDict):
			freqDict[char]+=1
		else:
			freqDict[char]=1
	for key in sorted(freqDict.keys()):
		print(key + ':' + str(freqDict[key])+' ', end='')
	print('\n')

fname = sys.argv[1]
seq = readSequence(fname)

n = len(seq)

seqList = []
for i in seq:
	seqList.append(i)

displayCount(seq)
residueSeq = resShuffle(seqList)
displayCount(residueSeq)

