

def find_max_length_palindrom(string):
	db = [[0 for x in range(len(string))] for y in range(len(string))]

	for x in range(len(string)):
		db[x][x] = 1

	first_index = 0
	total_len = 1
	for k in range(len(string) - 1):
	   if string[k] == string[k+1]:
	       db[k][k+1] = 1
	       first_index = k
	       total_len = 2
		
	for k in range(2, len(string)):
	   for i in range(len(string) - k):
	       j = i + k
	       if db[i + 1][j - 1] and string[i] == string[j]:
	          db[i][j] = 1
	          if (k+1 > total_len):
	          	first_index = i
	          	total_len = k+1
	
	return string[first_index:first_index+total_len]	




string = ['a','a','c','c','b','b','c','a']

print(find_max_length_palindrom(string))