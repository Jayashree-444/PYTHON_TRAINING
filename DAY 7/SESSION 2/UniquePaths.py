# For Right and Down
def unique_paths(m,n):
    # creating 2d Dp
    dp=[[0 for _ in range(n)] for _ in range(m)]
    # first row
    for i in range(n):
        dp[0][i]=1
    # first column
    for i in range(m):
        dp[i][0]=1
    # fill remainig cells
    for i in range(1,m):
        for j in range(1,n):
            # top               # left
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]
# sample inputs
m=3
n=2
# *(0,0) *(0,1)  # RDD,DRD,DDR
# *(1,0) *(1,1)
# *(2,0) *(2,1)
print(unique_paths(m,n))