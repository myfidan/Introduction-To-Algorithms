def find_absent(mylist):
	prev = 1
	for i in range(len(mylist)):
		if(prev == mylist[i][len(mylist[i])-1]):
			return i
		prev = mylist[i][len(mylist[i])-1]

number_list_1 = [
	[0], #0
	[1], #1
	[1,0], #2
	[1,1], #3
	[1,0,0], #4
	[1,0,1], #5
	[1,1,0], #6
	[1,1,1], #7
	[1,0,0,0], #8
	[1,0,0,1], #9
	[1,0,1,0], #10
	[1,1,0,0], #12
]	

number_list_2 = [
	[0], #0
	[1], #1
	[1,0], #2
	[1,1], #3
	[1,0,0], #4
	[1,0,1], #5
	[1,1,0], #6
	[1,1,1], #7
	[1,0,0,0], #8
	[1,0,1,0], #10
	[1,0,1,1], #11
]	


number_list_3 = [
	[0], #0
	[1,0], #2
	[1,1], #3
	[1,0,0], #4
	[1,0,1], #5
	[1,1,0], #6
	[1,1,1], #7
	[1,0,0,0], #8
	[1,0,0,1], #9
	[1,0,1,0], #10
	[1,0,1,1], #11
]	

print(find_absent(number_list_1)) ## 11 absent

print(find_absent(number_list_2)) ## 9 absent

print(find_absent(number_list_3)) ## 1 absent

