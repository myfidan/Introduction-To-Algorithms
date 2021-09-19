

def max_money(x,r,n,M):
	
	dp = [0 for i in range(M+1)]

	billboard = 0
	
	for i in range(1,M+1):
		if(billboard < n):
			if(x[billboard] != i):
				dp[i] = dp[i-1]
			else:
				
				if(i>=5): 
					dp[i] = max(dp[i-1],dp[i-5]+r[billboard]) 	
				else:
					dp[i] = r[billboard]	

				billboard += 1		
		else:
			dp[i] = dp[i-1]

	print_selected_miles(dp)		
	return dp[M]		

def print_selected_miles(dp):
	selected_miles = []
	i = len(dp)-2
	while i >= 0:
		if(dp[i] != dp[i+1]):
			selected_miles.append(i+1)
			i = i-4
		i-=1
		

	print(f'selected mile positions: {selected_miles}')		


M = 20
x = [3,7,12,13,14,17]
r = [7,6,5,3,1,6]

result = max_money(x,r,len(x),M)
print(f'Max earn money: {result}')