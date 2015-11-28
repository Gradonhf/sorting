# procedure bubbleSort( A : list of sortable items )
#    n = length(A)
#    repeat 
#      swapped = false
#      for i = 1 to n-1 inclusive do
#        /* if this pair is out of order */
#        if A[i-1] > A[i] then
#          /* swap them and remember something changed */
#          swap( A[i-1], A[i] )
#          swapped = true
#        end if
#      end for
#    until not swapped
# end procedure


def bubbleSort(sortList):
	length = len(sortList)
	for i in range(1,length):
		for j in range(i):	
			if sortList[i-1] > sortList[i]:
				sortList[i-1], sortList[i] = sortList[i], sortList[i-1]  
	return sortList
