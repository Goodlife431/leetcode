def isInterleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    
    # Check if the lengths of s1, s2, and s3 add up correctly
    if m + n != len(s3):
        return False
    
    # Create a 2D array to store the intermediate results
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base case
    dp[0][0] = True
    
    # Check if s1 matches with s3
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    # Check if s2 matches with s3
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    # Check if s1 and s2 interleaves to form s3
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    
    return dp[m][n]