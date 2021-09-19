
def findMinPath(triangle):
	row = len(triangle)-1
	dp = triangle[row]
	row -=1

	while(row>=0):
		for col in range(row+1):
			dp[col] = triangle[row][col] + min(dp[col],dp[col+1])
		row -= 1	
	print(dp[0])	


triangle = [
			[2],
			[5,4],
			[1,4,7],
			[8,6,9,6]
		]

findMinPath(triangle)		
