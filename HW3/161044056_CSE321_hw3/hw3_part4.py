import numpy as np


def quick_sort(mylist,low,high):
	total_count = 0
	if(low < high):
		piv,count = partition(mylist,low,high)
		total_count += count
		total_count +=quick_sort(mylist,low,piv-1)
		total_count +=quick_sort(mylist,piv+1,high)
	return total_count
		
def partition(mylist,low,high):
    i = ( low-1 )
    pivot = mylist[high]
    count =0
    for j in range(low , high):

        if   mylist[j] < pivot:
            i = i+1
            mylist[i],mylist[j] = mylist[j],mylist[i]
            count +=1


    mylist[i+1],mylist[high] = mylist[high],mylist[i+1]
    count +=1
    return ( i+1 ),count


def insertion_sort(mylist,low,high,count_insertion):

	for i in range(low,high+1):
		temp = mylist[i]
		j = i
		while(j>0 and temp < mylist[j-1]):
			count_insertion = count_insertion+1
			mylist[j] = mylist[j-1]
			j -= 1
		mylist[j] = temp
	return count_insertion		




insertion_avg = 0
quick_avg = 0


for i in range(50):
	

	arr = np.random.randint(1,100,10)
	arr2 = arr.copy()
	insertion_avg += insertion_sort(arr,0,len(arr)-1,0)
	quick_avg += quick_sort(arr2,0,len(arr2)-1)

print(f'insertion sort average = {insertion_avg/50.0}')
print(f'quick sort average = {quick_avg/50.0}')
