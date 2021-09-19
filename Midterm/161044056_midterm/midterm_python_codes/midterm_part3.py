
def quick_sort(mylist,low,high):
	if(low < high):
		if(high-low < 5):
			insertion_sort(my_list,low,high)
		else:
			piv = partition(mylist,low,high)
			quick_sort(mylist,low,piv-1)
			quick_sort(mylist,piv+1,high)

def partition(mylist,low,high):
	left = low
	right = high
	pivot = mylist[low]

	while(left < right):

		while(left < right and mylist[left] <= pivot):
			left += 1
		while(mylist[right] > pivot):
			right -= 1	

		if(left < right):
			
			temp = mylist[left]
			mylist[left] = mylist[right]
			mylist[right] = temp	

	
	mylist[low] = mylist[right]
	mylist[right] = pivot		

	return right


def insertion_sort(mylist,low,high):

	for i in range(low,high+1):
		temp = mylist[i]
		j = i
		while(j>0 and temp < mylist[j-1]):
			mylist[j] = mylist[j-1]
			j -= 1
		mylist[j] = temp	



my_list = [4,1,2,1,7,9,11,23,5,7,4,22,1,2,3,7,3,3,43,12] #len 20
quick_sort(my_list,0,len(my_list)-1)
print(my_list)