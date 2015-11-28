#!/usr/bin/python
from bubblesort import bubbleSort

def bubbleTest ():
	bubble_list = [3,5,2,7,1]
	print "Before Sort:\t", bubble_list
	for i in range (1,len(bubble_list)):
		bubbleSort(bubble_list)
	print "After Sort: \t", bubble_list

def insertionTest ():
	insertion_list = [3,5,2,7,1]
	print "Before Sort:\t", insertion_list
	for i in range (1,len(insertion_list)):
		insertionSort(insertion_list)
	print "After Sort: \t", insertion_list

def main ():
	bubbleTest()
	insertionTest()
main()