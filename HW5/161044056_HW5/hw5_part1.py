


dp = [[0 for x in range(100)] for y in range(50)]
visit = [[0 for x in range(100)] for y in range(50)]

  
maxSum = 100
MaxArrSize = 50
def Check_subset_zero(i, s, arr, n) : 
      
    # Base cases  
    if (i == n) : 
        if (s == 0) : 
            return 1;  
        else : 
            return 0;  
      
    if (visit[i][s + MaxArrSize]) : 
        return dp[i][s + MaxArrSize];  
  
    visit[i][s + MaxArrSize] = 1;  
    dp[i][s + MaxArrSize ] = (Check_subset_zero(i + 1, s + arr[i], arr, n) + Check_subset_zero(i + 1, s, arr, n));  
    return dp[i][s + MaxArrSize];  
  

arr = [2,3,-5,-8,6,-1];  
print(Check_subset_zero(0, 0, arr, len(arr))-1);  