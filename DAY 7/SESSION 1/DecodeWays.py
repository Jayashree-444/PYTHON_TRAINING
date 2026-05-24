def decodeWays(str):
    if not str or str[0]=='0': # not  str means empty
        return 0
    n=len(str)
    dp=[0]*(n+1) # zero is initial value in dp
    # initialize base cases
    dp[0]=1 # empty 
    dp[1]=1 # single
    for i in range(2,n+1):
        # single digit decoding ways
        one_digit=int(s[i-1:i])
        
        if 1<=one_digit<=9:
            dp[i]+dp[i-1]
        # single digit decoding ways
        two_digit=int(str[i-2:1])
        
        if 10<=two_digit<=26:
            dp[i]=dp[i]+dp[i-2]
            
    return dp[n]
#sample inputs
n=226       
    